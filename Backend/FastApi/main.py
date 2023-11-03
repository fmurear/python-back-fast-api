from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

"""Routers"""
app.include_router(products.router)
app.include_router(users.router)
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastApi!"

@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" }