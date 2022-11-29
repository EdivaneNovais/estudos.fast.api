from typing import Dict, List, Optional

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from time import sleep

from models import Curso
from models import cursos


def fake_db():
    try:
        print("Abrindo conexão com banco de dados...")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados...")
        sleep(1)

app = FastAPI(
    title='API de cursos da Geek University',
    version='0.0.1',
    description='Uma API ára estudo do Fastapi'
)

# cursos = {
#     1: {
#         "titulo" : "Programação para leigos",
#         "aulas": 112,
#         "horas": 58
#     },
#     2: {
#         "titulo": "Algoritmos e lógica de Programação",
#         "aulas": 87,
#         "horas": 67
        
#     }
    
# }

@app.get('/cursos', description='Retorna todos os cursos ou uma lista vazia', 
         summary='Retorna todos os cursos', 
         response_model=List[Curso],#pega todos os dados
         response_description='Cursos encontados com sucesso.')
async def get_cursos(db: any = Depends(fake_db)):#injeção de dependencia
    return cursos

@app.get('/cursos/{curso_id}')#trás dados especificos
async def get_curso(curso_id:int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0 , lt=3), db: any = Depends(fake_db)):#path parameters
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='CURSO NÃO ENCONTRADO')
    
@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    # if curso.id not in cursos:
    next_id: int = len(cursos) + 1
    # cursos[next_id] = curso
    # del curso.id
    curso.id = next_id
    cursos.append(curso)
    return curso
    # else:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, defail="Já existe um curso com ID {curso.id}.")


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id {curso_id}')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id {curso_id}')


@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):#query parameters
    # soma= a + b + c
    soma: int = a + b
    if c:
        soma = soma + c
    print(f'X-GEEK: {x_geek}')
    
    return {"resultado": soma}


if __name__ == '__main__':
    import uvicorn  
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)