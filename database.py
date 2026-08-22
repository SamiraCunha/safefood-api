# Responsavel pela infraestrutura da base de dados:
# 1. obter DATABASE_URL 
# 2. criar Engine
# 3. criar Base
# 4. preparar mecanismo de sessão
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker


load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

database_url = os.environ["DATABASE_URL"] # Eu tinha os.getenv mas alterei para os.environ para que o erro seja mais explícito caso a variável não esteja definida.

engine = create_engine(database_url)


Session = sessionmaker(engine)



class Base(DeclarativeBase): 
    pass


