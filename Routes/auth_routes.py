from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.get("/")
async def auth():
    """
    Essa é a rota padrão para autenticação.
    
    """
    return {"status": "ok", "message": "Rota de autenticação funcionando!"}