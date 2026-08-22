from fastapi import APIRouter

products_router = APIRouter(prefix="/products", tags=["Products"])

#como criar uma rota no fast Api

@products_router.get("/")
async def products():
    """
    Essa é a rota padrão para produtos.
    
    """
    return {"status": "ok", "message": "Rota de produtos funcionando!"}