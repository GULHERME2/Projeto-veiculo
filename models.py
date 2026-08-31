# from pydantic import BaseModel


# class Veiculo(BaseModel):
#     id: int
#     modelo: str
#     placa: str
#     quilometragem: float
#     marca_id: int

from pydantic import BaseModel


class Marca(BaseModel):
    id:int
    nome:str
    ativa:bool

class Veiculo(BaseModel):
    id:int
    modelo:str
    placa:str
    quilometragem:float
    marca_id:int


