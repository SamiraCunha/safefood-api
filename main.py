from fastapi import FastAPI

app = FastAPI(
    title="SafeFood FastAPI",
    description="API para gestão e alertas de validade de alimentos",
    version="0.1.0",
) 

#Criei depois para não dar problema de importação circular
from Routes.auth_routes import auth_router
from Routes.products_routes import products_router

app.include_router(auth_router)
app.include_router(products_router)

