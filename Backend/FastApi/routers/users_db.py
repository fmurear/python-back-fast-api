"""Módulos a importar"""
from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema 
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND : {"message": "No encontrado"}})

@router.get("/", response_model= list[User])
async def users():
    """Función que devuelve todos los usuarios"""
    return users_schema(db_client.users.find())

# Path y Query param
@router.get("/{id}", response_model=User)
async def user_path(id: str):
    """Función que devuelve todos los usuarios por id"""
    return search_user('_id', ObjectId(id))

#Query param    
@router.get("/query/", response_model=User)
async def user_query(id: str):
    """Función que devuelve todos los usuarios por id"""
    return search_user('_id', ObjectId(id))

@router.post("/", response_model= User, status_code=status.HTTP_201_CREATED )
async def user(user: User):
    """Función para añadir usuario"""
    if type(search_user('email',user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id": ObjectId(id)}))

    return User(**new_user)

@router.put("/", response_model=User)
async def user(user: User):
    """Función para actualizar el usuario"""
    user_dict = dict(user)
    del user_dict["id"]
    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    print(user.id)
    return search_user('_id',ObjectId(user.id))

@router.delete("/{id}")
async def user(id: str, status_code=status.HTTP_204_NO_CONTENT):
    """Función para eliminar un usuario"""
    found = db_client.users.find_one_and_delete({"_id":ObjectId(id)})
    
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")

def search_user(field: str, value):
    """Función que devuelve todos los usuarios por field y si no existe retorna un error"""
    try:
        return User(**user_schema(db_client.users.find_one({field: value})))
    except:
        return {"error": "Ha ocurrido un error al buscar el usuario por {field}"}
    