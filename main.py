from fastapi import FastAPI

app = FastAPI(
    title="SafeFood API",
    description="API para gestão e alertas de validade de alimentos",
    version="0.1.0",
) 

# Endpoint inicial de teste

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API SafeFood está funcionando!"}