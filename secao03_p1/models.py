from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        #validacao 1
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras.')
        
        #validacao 2
        if value.islower():
            raise ValueError('O titulo deve ser capitalizado.')
        
        return value
        
    
cursos = [
    Curso(id=1, titulo='Programação para leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Programação em python', aulas=52, horas=66)
    
]