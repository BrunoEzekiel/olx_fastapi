from fastapi import FastAPI
from src.schemas.schemas import Produto


app = FastAPI()

@app.post("/produtos")
def criar_produto(produto: Produto):
    return {"mensagem": "Produto criado com sucesso"}

@app.get("/produtos")
def listar_produtos():
    return {"mensagem": "Listando os produtos"}

@app.get("/produtos/{id}")
def buscar_produto(id: int):
    return {"mensagem": f"Buscando o produto com id {id}"}

@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto):
    return {"mensagem": f"Atualizando o produto com id {id}"}

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    return {"mensagem": f"Deletando o produto com id {id}"}

# Compare this snippet from src/infra/sqlalchemy/repositorios/user.py:
# from sqlalchemy.orm import Session
# from src.schemas import schemas
# from src.infra.sqlalchemy.models import models
# #classe que vai ser responsável por fazer a comunicação com o banco de dados
# class RepositorioUser():
#     #método construtor
#     def __init__(self, db: Session):