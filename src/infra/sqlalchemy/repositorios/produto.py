from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
#classe que vai ser responsável por fazer a comunicação com o banco de dados
class RepositorioProduto():
    #método construtor
    def __init__(self, db: Session):
        self.db = db
    
    #método para salvar um produto
    def salvar(self, produto: schemas.Produto):
        db_produto = models.Produto(name=produto.name,  description=produto.description, 
        price=produto.price, disponivel=produto.disponivel)
        #operação no nosso banco de dados
        self.db.add(db_produto)#adiciona o produto no banco de dados
        self.db.commit()#salva a operação
        self.db.refresh(db_produto)#atualiza o banco de dados
        return db_produto#retorna o produto salvo
    #método para listar os produtos 
    def listar(self):#método para listar os produtos
        produtos = self.db.query(models.Produto).all()
        return produtos
    #método para buscar um produto pelo id
     # Método para buscar um produto pelo id
    def buscar_por_id(self, id: int):
        produto = self.db.query(models.Produto).filter(models.Produto.id == id).first()
        return produto

    # Método para atualizar um produto
    def atualizar(self, id: int, produto: schemas.Produto):
        db_produto = self.db.query(models.Produto).filter(models.Produto.id == id).first()
        if db_produto:
            db_produto.name = produto.name
            db_produto.description = produto.description
            db_produto.price = produto.price
            db_produto.disponivel = produto.disponivel
            self.db.commit()
            self.db.refresh(db_produto)
            return db_produto
        return None

    # Método para deletar um produto
    def deletar(self, id: int):
        db_produto = self.db.query(models.Produto).filter(models.Produto.id == id).first()
        if db_produto:
            self.db.delete(db_produto)
            self.db.commit()
            return db_produto
        return None