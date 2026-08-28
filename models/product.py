from database import Base
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, index=True)
    quantity: Mapped[int] = mapped_column(default=1)
    data_validade: Mapped[date] = mapped_column(Date, nullable=False)