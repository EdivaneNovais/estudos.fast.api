from typing import Optional

from pydantic import BaseModel as SCBaseModel#chamo ele dessa foma pois o proprimo sqlachemy tem seu BaseModel

class CursoSchema(SCBaseModel):
    ID: Optional[int]#id vai ser informado pelo proprio banco de dados
    titulo: str
    aulas: int
    horas: int
    
    class Config:
        orm_mode = True