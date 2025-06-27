from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a mi API con FastAPI"}


class Usuario(BaseModel):
    id: int
    nombre: str

usuarios = [
    Usuario(id=1, nombre="Jeremy"),
    Usuario(id=2, nombre="John")
]

@app.get("/hola")
def saludar():
    return {"mensaje": "¡Hola, mundo!"}

@app.get("/usuarios", response_model=List[Usuario])
def obtener_usuarios():
    return usuarios

@app.post("/usuarios", response_model=Usuario)
def crear_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario
