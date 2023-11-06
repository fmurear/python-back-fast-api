from pydantic import BaseModel

class User(BaseModel):
    """Clase para declarar el usuario"""
    id: str | None
    username: str
    email: str