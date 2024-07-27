from pydantic import BaseModel # Importando a classe BaseModel do módulo pydantic
from typing import Optional, List

class User(BaseModel): # Definindo a classe User que herda de BaseModel
    id: Optional[str] = None # Atributo id do tipo str que é opcional
    name: str # Atributo name do tipo str
    phone: str  # Atributo phone do tipo str
    meus_produtos: List['Produto'] # Atributo meus_produtos do tipo List[Pedido]
    minhas_vendas: List['Pedido'] # Atributo minhas_vendas do tipo List[Pedido]
    minhas_compras: List['Pedido'] # Atributo minhas_compras do tipo List[Pedido]
    
# Definindo a classe Produto que herda de BaseModel    
class Produto(BaseModel):
    id: Optional[str] = None # Atributo id do tipo str que é opcional
    User: 'User' # Atributo User do tipo User
    name: str # Atributo name do tipo str
    description: str # Atributo description do tipo str
    price: float # Atributo price do tipo float
    disponivel: bool = False # Atributo disponivel do tipo bool que é False por padrão
    
    class Config: # Definindo a classe Config
        orm_mode = True # Atributo orm_mode que é True

class Pedido(BaseModel): # Definindo a classe Pedido que herda de BaseModel
    id: Optional[str] = None
    user: 'User'
    produtos: list[Produto]
    quantidade: int
    entrega: bool = True
    endereco: str
    observacao: Optional [str] = 'Sem observações'



    