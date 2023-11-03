"""Módulo a importar"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

## Entidad User
class User(BaseModel):
    """Clase para declarar el usuario"""
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
                User(id= 1,
                     name="Francisco",
                     surname="Muñoz-Reja",
                     url="http://loquemesalgalapolla1.com",
                     age=20),
                User(id= 2,
                     name="Manuel",
                     surname="Muñoz-Reja",
                     url="http://loquemesalgalapolla2.com",
                     age=21),
                User(id= 3,
                     name="Laura",
                     surname="Rejas",
                     url="http://loquemesalgalapolla3.com",
                     age=22),
             ]
@router.get("/users")
async def users():
    """Función que devuelve todos los usuarios"""
    return users_list

# Path y Query param
@router.get("/user/{id}")
async def user_path(id: int):
    """Función que devuelve todos los usuarios por id"""
    return search_user(id)

#Query param    
@router.get("/userquery/")
async def user_query(id: int):
    """Función que devuelve todos los usuarios por id"""
    return search_user(id)

@router.post("/users", response_model= User, status_code=201 )
async def user(user: User):
    """Función para añadir usuario"""
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    users_list.append(user)

@router.put("/user/")
async def user(user: User):
    """Función para actualizar el usuario"""
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    
    return user

@router.delete("/user/{id}")
async def user(id: int):
    """Función para eliminar un usuario"""
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}

def search_user(id):
    """Función que devuelve todos los usuarios por id y si no existe retorna un error"""
    try:
        return filter( lambda user: user.id == id, users_list)
    except:
        return {"error": "No se ha encontrado usuario"}