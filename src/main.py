from fastapi import FastAPI
from routers import (
    usuario_router,
    categoria_router,
    habito_router,
    frequencia_router,
    notificacao_router,
    objetivo_router,
    dados_usuario_router,
    sugestao_router,
    feedback_router
)

app = FastAPI(title="Hábito e Objetivos API", version="1.0.0")

# Include routers
app.include_router(usuario_router, tags=["Usuários"])
app.include_router(categoria_router, tags=["Categorias"])
app.include_router(habito_router, tags=["Hábitos"])
app.include_router(frequencia_router, tags=["Frequências"])
app.include_router(notificacao_router, tags=["Notificações"])
app.include_router(objetivo_router, tags=["Objetivos"])
app.include_router(dados_usuario_router, tags=["Dados do Usuário"])
app.include_router(sugestao_router, tags=["Sugestões"])
app.include_router(feedback_router, tags=["Feedbacks"])

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Hábito e Objetivos!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)