from sqlalchemy.orm import Session
from src.schemas import Produto, schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db
        self.session = db.session

    def salvar(self, produto: schemas.Produto):
        db_produto = models.Produto(name=produto.name, description=produto.description, price=produto.price, disponivel=produto.disponivel)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
        

    def listar(self):
        produtos = self.session.query(Produto).all()
        return produtos
    
    def buscar_por_id(self, id):
        pass

   

    def atualizar(self, produto):
       pass

    def deletar(self, produto):
        pass