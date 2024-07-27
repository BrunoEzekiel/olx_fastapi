from pydantic import BaseModel
from typing import List, Optional
from . import Pedido

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    meus_produtos: List[Pedido]
    minhas_vendas: List[Pedido]
    minhas_compras: List[Pedido]
    
    
class Produto(BaseModel):
    id: Optional[str] = None
    User: User
    name: str
    description: str
    price: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    user: 'User'
    produtos: 'Produto'
    quantidade: int
    entrega: bool = True
    endereco: str
    observacao: Optional [str] = 'Sem observações'



    