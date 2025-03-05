from fastapi import FastAPI, HTTPException
from database import database

app = FastAPI()

db = database

@app.get("/")
def root():
    return {"mensagem": "Bem Vindo"}

@app.get("/restaurante")
def buscar_restaurante(nome : str):
    for restaurante in db:
        if restaurante["nome_restaurante"] == nome:
            return restaurante
    else:
        raise HTTPException(404, detail="Restaurante não encontrado")

@app.get("/{nome}/cardapio")
def buscar_cardapio(nome : str):
    if not nome:
        return {"Erro": "É preciso inserir o nome do restaurante"}

    for restaurante in db:
        if restaurante["nome_restaurante"] == nome:
            return restaurante
    else:
        raise HTTPException(404, detail="Restaurante não encontrado")