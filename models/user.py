from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, index=True)
    # Mapped[Optional[str]] avisa ao Python e ao SQLAlchemy que o campo pode ser Nulo
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, index=True) # não coloquei nullable=false porque para esta fase do projeto o email não é obrigatório
    hashed_password: Mapped[str] = mapped_column(String)
    ativo: Mapped[bool] = mapped_column(default=True)
    admin: Mapped[bool] = mapped_column(default=False)

 




    #formato legado
    # id = Column("id", Integer, primary_key=True, index=True)
    # name = Column("name", String, index=True)
    # email = Column("email", String, unique=True, index=True)
    # hashed_password = Column("hashed_password", String)
    # ativo = Column("ativo", Boolean, default=True)
    # admin = Column("admin", Boolean, default=False)