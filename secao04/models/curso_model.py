from core.configs import settings

from sqlalchemy import column, Integer, String

class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    
    id: int = column(Integer, primary_key=True, autoincrement=True)
    titulo: str = column(String(100))
    aulas: int = column(Integer)
    horas: int = column(Integer)