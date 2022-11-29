from core.configs import settings
from core.database import engine

async def create_tables() -> None:
    import models.__al_models #pra que coloque na memoria todos os models que são sqlalchemy
    print("criando as tabelas no banco de dados...")
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)#caso tenha alguma alteração
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)#criar
    print("Tabelas criadas com sucesso.")
    
if __name__ == '__main__':#bloco de execuçao
    import asyncio
    
    asyncio.run(create_tables())