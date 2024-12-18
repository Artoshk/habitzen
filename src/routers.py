from fastapi import APIRouter, HTTPException, Depends
from schemas import Usuario, Categoria, Habito, Frequencia, Notificacao, Objetivo, DadosUsuario, Sugestao, FeedbackIA

# Routers
usuario_router = APIRouter()

@usuario_router.post("/usuarios/", response_model=Usuario)
def create_usuario(usuario: Usuario):
    return Usuario.create(**usuario.dict())

@usuario_router.delete("/usuarios/{id_usuario}", response_model=dict)
def delete_usuario(id_usuario: int):
    return Usuario.delete(id_usuario)

@usuario_router.put("/usuarios/{id_usuario}", response_model=dict)
def update_usuario(id_usuario: int, usuario: Usuario):
    return Usuario.update(id_usuario, **usuario.dict())

@usuario_router.get("/usuarios/{id_usuario}", response_model=Usuario)
def get_usuario(id_usuario: int):
    return Usuario.get(id_usuario)

categoria_router = APIRouter()

@categoria_router.post("/categorias/", response_model=Categoria)
def create_categoria(categoria: Categoria):
    return Categoria.create(**categoria.dict())

@categoria_router.delete("/categorias/{id_categoria}", response_model=dict)
def delete_categoria(id_categoria: int):
    return Categoria.delete(id_categoria)

@categoria_router.put("/categorias/{id_categoria}", response_model=dict)
def update_categoria(id_categoria: int, categoria: Categoria):
    return Categoria.update(id_categoria, **categoria.dict())

@categoria_router.get("/categorias/{id_categoria}", response_model=Categoria)
def get_categoria(id_categoria: int):
    return Categoria.get(id_categoria)

habito_router = APIRouter()

@habito_router.post("/habitos/", response_model=Habito)
def create_habito(habito: Habito):
    return Habito.create(**habito.dict())

@habito_router.delete("/habitos/{id_habito}", response_model=dict)
def delete_habito(id_habito: int):
    return Habito.delete(id_habito)

@habito_router.put("/habitos/{id_habito}", response_model=dict)
def update_habito(id_habito: int, habito: Habito):
    return Habito.update(id_habito, **habito.dict())

@habito_router.get("/habitos/{id_habito}", response_model=Habito)
def get_habito(id_habito: int):
    return Habito.get(id_habito)

frequencia_router = APIRouter()

@frequencia_router.post("/frequencias/", response_model=Frequencia)
def create_frequencia(frequencia: Frequencia):
    return Frequencia.create(**frequencia.dict())

@frequencia_router.delete("/frequencias/{id_frequencia}", response_model=dict)
def delete_frequencia(id_frequencia: int):
    return Frequencia.delete(id_frequencia)

@frequencia_router.put("/frequencias/{id_frequencia}", response_model=dict)
def update_frequencia(id_frequencia: int, frequencia: Frequencia):
    return Frequencia.update(id_frequencia, **frequencia.dict())

@frequencia_router.get("/frequencias/{id_frequencia}", response_model=Frequencia)
def get_frequencia(id_frequencia: int):
    return Frequencia.get(id_frequencia)

notificacao_router = APIRouter()

@notificacao_router.post("/notificacoes/", response_model=Notificacao)
def create_notificacao(notificacao: Notificacao):
    return Notificacao.create(**notificacao.dict())

@notificacao_router.delete("/notificacoes/{id_notificacao}", response_model=dict)
def delete_notificacao(id_notificacao: int):
    return Notificacao.delete(id_notificacao)

@notificacao_router.put("/notificacoes/{id_notificacao}", response_model=dict)
def update_notificacao(id_notificacao: int, notificacao: Notificacao):
    return Notificacao.update(id_notificacao, **notificacao.dict())

@notificacao_router.get("/notificacoes/{id_notificacao}", response_model=Notificacao)
def get_notificacao(id_notificacao: int):
    return Notificacao.get(id_notificacao)

objetivo_router = APIRouter()

@objetivo_router.post("/objetivos/", response_model=Objetivo)
def create_objetivo(objetivo: Objetivo):
    return Objetivo.create(**objetivo.dict())

@objetivo_router.delete("/objetivos/{id_objetivo}", response_model=dict)
def delete_objetivo(id_objetivo: int):
    return Objetivo.delete(id_objetivo)

@objetivo_router.put("/objetivos/{id_objetivo}", response_model=dict)
def update_objetivo(id_objetivo: int, objetivo: Objetivo):
    return Objetivo.update(id_objetivo, **objetivo.dict())

@objetivo_router.get("/objetivos/{id_objetivo}", response_model=Objetivo)
def get_objetivo(id_objetivo: int):
    return Objetivo.get(id_objetivo)

dados_usuario_router = APIRouter()

@dados_usuario_router.post("/dados_usuario/", response_model=DadosUsuario)
def create_dados_usuario(dados_usuario: DadosUsuario):
    return DadosUsuario.create(**dados_usuario.dict())

@dados_usuario_router.delete("/dados_usuario/{id_usuario}", response_model=dict)
def delete_dados_usuario(id_usuario: int):
    return DadosUsuario.delete(id_usuario)

@dados_usuario_router.put("/dados_usuario/{id_usuario}", response_model=dict)
def update_dados_usuario(id_usuario: int, dados_usuario: DadosUsuario):
    return DadosUsuario.update(id_usuario, **dados_usuario.dict())

@dados_usuario_router.get("/dados_usuario/{id_usuario}", response_model=DadosUsuario)
def get_dados_usuario(id_usuario: int):
    return DadosUsuario.get(id_usuario)

sugestao_router = APIRouter()

@sugestao_router.post("/sugestoes/", response_model=Sugestao)
def create_sugestao(sugestao: Sugestao):
    return Sugestao.create(**sugestao.dict())

@sugestao_router.delete("/sugestoes/{id_sugestao}", response_model=dict)
def delete_sugestao(id_sugestao: int):
    return Sugestao.delete(id_sugestao)

@sugestao_router.put("/sugestoes/{id_sugestao}", response_model=dict)
def update_sugestao(id_sugestao: int, sugestao: Sugestao):
    return Sugestao.update(id_sugestao, **sugestao.dict())

@sugestao_router.get("/sugestoes/{id_sugestao}", response_model=Sugestao)
def get_sugestao(id_sugestao: int):
    return Sugestao.get(id_sugestao)

feedback_router = APIRouter()

@feedback_router.post("/feedbacks/", response_model=FeedbackIA)
def create_feedback(feedback: FeedbackIA):
    return FeedbackIA.create(**feedback.dict())

@feedback_router.delete("/feedbacks/{id_feedback}", response_model=dict)
def delete_feedback(id_feedback: int):
    return FeedbackIA.delete(id_feedback)

@feedback_router.put("/feedbacks/{id_feedback}", response_model=dict)
def update_feedback(id_feedback: int, feedback: FeedbackIA):
    return FeedbackIA.update(id_feedback, **feedback.dict())

@feedback_router.get("/feedbacks/{id_feedback}", response_model=FeedbackIA)
def get_feedback(id_feedback: int):
    return FeedbackIA.get(id_feedback)