"""Módulo a importar"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
@app.get("/users")
async def users():
    """Función que devuelve todos los usuarios"""
    return users_list

# Path y Query param
@app.get("/user/{id}")
async def user_path(id: int):
    """Función que devuelve todos los usuarios por id"""
    return search_user(id)

#Query param    
@app.get("/userquery/")
async def user_query(id: int):
    """Función que devuelve todos los usuarios por id"""
    return search_user(id)

def search_user(id):
    """Función que devuelve todos los usuarios por id y si no existe retorna un error"""
    try:
        return filter( lambda user: user.id == id, users_list)
    except:
        return {"error": "No se ha encontrado usuario"}