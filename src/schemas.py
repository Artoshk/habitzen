from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enums import RecorrenciaEnum, ObjetivoPrioridadeEnum, ObjetivoStatusEnum, SugestaoTipoEnum
import os
import psycopg2
from dotenv import load_dotenv
from fastapi import HTTPException
from fastapi.responses import JSONResponse

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)


# Schemas
class Usuario(BaseModel):
    id_usuario: Optional[int]
    nome: str
    email: str
    senha_hash: str
    data_criacao: Optional[datetime]

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO usuario (nome, email, senha_hash, data_criacao)
                VALUES (%s, %s, %s, %s) RETURNING id_usuario;
                """,
                (kwargs['nome'], kwargs['email'], kwargs['senha_hash'], kwargs.get('data_criacao'))
            )
            id_usuario = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_usuario": id_usuario, **kwargs})

    @classmethod
    def delete(cls, id_usuario):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_usuario, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_usuario)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE usuario SET {set_clause} WHERE id_usuario = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Usuario updated successfully"})

    @classmethod
    def get(cls, id_usuario):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
            user = cursor.fetchone()
            if user:
                return JSONResponse(status_code=200, content={"id_usuario": user[0], "nome": user[1], "email": user[2]})
            raise HTTPException(status_code=404, detail="Usuario not found")

class Categoria(BaseModel):
    id_categoria: Optional[int]
    nome: str
    cor: Optional[str] = "#FFFFFF"

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO categoria (nome, cor)
                VALUES (%s, %s) RETURNING id_categoria;
                """,
                (kwargs['nome'], kwargs.get('cor', '#FFFFFF'))
            )
            id_categoria = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_categoria": id_categoria, **kwargs})

    @classmethod
    def delete(cls, id_categoria):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (id_categoria,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_categoria, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_categoria)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE categoria SET {set_clause} WHERE id_categoria = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Categoria updated successfully"})

    @classmethod
    def get(cls, id_categoria):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM categoria WHERE id_categoria = %s", (id_categoria,))
            category = cursor.fetchone()
            if category:
                return JSONResponse(status_code=200, content={"id_categoria": category[0], "nome": category[1], "cor": category[2]})
            raise HTTPException(status_code=404, detail="Categoria not found")

class Habito(BaseModel):
    id_habito: Optional[int]
    id_usuario: int
    id_categoria: Optional[int]
    nome: str
    descricao: Optional[str]
    meta: Optional[int] = 1
    unidade: Optional[str] = "vezes"
    recorrencia: Optional[RecorrenciaEnum] = RecorrenciaEnum.diario
    ativo: Optional[bool] = True
    data_criacao: Optional[datetime]

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO habito (id_usuario, id_categoria, nome, descricao, meta, unidade, recorrencia, ativo, data_criacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_habito;
                """,
                (kwargs['id_usuario'], kwargs.get('id_categoria'), kwargs['nome'], kwargs.get('descricao'), 
                 kwargs.get('meta', 1), kwargs.get('unidade', 'vezes'), kwargs.get('recorrencia', 'diario'), 
                 kwargs.get('ativo', True), kwargs.get('data_criacao'))
            )
            id_habito = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_habito": id_habito, **kwargs})

    @classmethod
    def delete(cls, id_habito):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM habito WHERE id_habito = %s", (id_habito,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_habito, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_habito)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE habito SET {set_clause} WHERE id_habito = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Habito updated successfully"})

    @classmethod
    def get(cls, id_habito):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM habito WHERE id_habito = %s", (id_habito,))
            habit = cursor.fetchone()
            if habit:
                return JSONResponse(status_code=200, content={"id_habito": habit[0], "nome": habit[3], "descricao": habit[4]})
            raise HTTPException(status_code=404, detail="Habito not found")

class Frequencia(BaseModel):
    id_frequencia: Optional[int]
    id_habito: int
    data: datetime
    progresso: Optional[int] = 0
    concluido: Optional[bool] = False

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO frequencia (id_habito, data, progresso, concluido)
                VALUES (%s, %s, %s, %s) RETURNING id_frequencia;
                """,
                (kwargs['id_habito'], kwargs['data'], kwargs.get('progresso', 0), kwargs.get('concluido', False))
            )
            id_frequencia = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_frequencia": id_frequencia, **kwargs})

    @classmethod
    def delete(cls, id_frequencia):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM frequencia WHERE id_frequencia = %s", (id_frequencia,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_frequencia, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_frequencia)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE frequencia SET {set_clause} WHERE id_frequencia = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Frequencia updated successfully"})

    @classmethod
    def get(cls, id_frequencia):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM frequencia WHERE id_frequencia = %s", (id_frequencia,))
            frequency = cursor.fetchone()
            if frequency:
                return JSONResponse(status_code=200, content={"id_frequencia": frequency[0], "data": frequency[2], "progresso": frequency[3]})
            raise HTTPException(status_code=404, detail="Frequencia not found")

class Notificacao(BaseModel):
    id_notificacao: Optional[int]
    id_habito: int
    horario: datetime
    mensagem: Optional[str] = "Hora de cumprir seu hábito!"
    ativo: Optional[bool] = True

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO nofificacao (id_habito, horario, mensagem, ativo)
                VALUES (%s, %s, %s, %s) RETURNING id_notificacao;
                """,
                (kwargs['id_habito'], kwargs['horario'], kwargs.get('mensagem', 'Hora de cumprir seu hábito!'), kwargs.get('ativo', True))
            )
            id_notificacao = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_notificacao": id_notificacao, **kwargs})

    @classmethod
    def delete(cls, id_notificacao):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM nofificacao WHERE id_notificacao = %s", (id_notificacao,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_notificacao, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_notificacao)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE nofificacao SET {set_clause} WHERE id_notificacao = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Notificacao updated successfully"})

    @classmethod
    def get(cls, id_notificacao):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM nofificacao WHERE id_notificacao = %s", (id_notificacao,))
            notification = cursor.fetchone()
            if notification:
                return JSONResponse(status_code=200, content={"id_notificacao": notification[0], "mensagem": notification[3]})
            raise HTTPException(status_code=404, detail="Notificacao not found")

class Objetivo(BaseModel):
    id_objetivo: Optional[int]
    id_usuario: int
    descricao: str
    prioridade: Optional[ObjetivoPrioridadeEnum] = ObjetivoPrioridadeEnum.media
    status: Optional[ObjetivoStatusEnum] = ObjetivoStatusEnum.ativo
    data_criacao: Optional[datetime]

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO objetivo (id_usuario, descricao, prioridade, status, data_criacao)
                VALUES (%s, %s, %s, %s, %s) RETURNING id_objetivo;
                """,
                (kwargs['id_usuario'], kwargs['descricao'], kwargs.get('prioridade', 'media'), kwargs.get('status', 'ativo'), kwargs.get('data_criacao'))
            )
            id_objetivo = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_objetivo": id_objetivo, **kwargs})

    @classmethod
    def delete(cls, id_objetivo):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM objetivo WHERE id_objetivo = %s", (id_objetivo,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_objetivo, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_objetivo)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE objetivo SET {set_clause} WHERE id_objetivo = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Objetivo updated successfully"})

    @classmethod
    def get(cls, id_objetivo):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM objetivo WHERE id_objetivo = %s", (id_objetivo,))
            objective = cursor.fetchone()
            if objective:
                return JSONResponse(status_code=200, content={"id_objetivo": objective[0], "descricao": objective[2]})
            raise HTTPException(status_code=404, detail="Objetivo not found")

class DadosUsuario(BaseModel):
    id_usuario: int
    idade: Optional[int]
    peso: Optional[float]
    altura: Optional[float]
    condicoes_saude: Optional[str]
    preferencias: Optional[str]

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO dados_usuario (id_usuario, idade, peso, altura, condicoes_saude, preferencias)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                (kwargs['id_usuario'], kwargs.get('idade'), kwargs.get('peso'), kwargs.get('altura'), kwargs.get('condicoes_saude'), kwargs.get('preferencias'))
            )
            conn.commit()
            return JSONResponse(status_code=201, content={"message": "DadosUsuario created successfully"})

    @classmethod
    def delete(cls, id_usuario):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM dados_usuario WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_usuario, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_usuario)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE dados_usuario SET {set_clause} WHERE id_usuario = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "DadosUsuario updated successfully"})

    @classmethod
    def get(cls, id_usuario):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM dados_usuario WHERE id_usuario = %s", (id_usuario,))
            data = cursor.fetchone()
            if data:
                return JSONResponse(status_code=200, content={"id_usuario": data[0], "idade": data[1], "peso": data[2], "altura": data[3]})
            raise HTTPException(status_code=404, detail="DadosUsuario not found")

class Sugestao(BaseModel):
    id_sugestao: Optional[int]
    id_usuario: int
    tipo: SugestaoTipoEnum
    mensagem: str
    data_sugestao: Optional[datetime]
    aceita: Optional[bool]

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO sugestao (id_usuario, tipo, mensagem, aceita)
                VALUES (%s, %s, %s, %s) RETURNING id_sugestao;
                """,
                (kwargs['id_usuario'], kwargs['tipo'], kwargs['mensagem'], kwargs.get('aceita'))
            )
            id_sugestao = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_sugestao": id_sugestao, **kwargs})

    @classmethod
    def delete(cls, id_sugestao):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM sugestao WHERE id_sugestao = %s", (id_sugestao,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_sugestao, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_sugestao)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE sugestao SET {set_clause} WHERE id_sugestao = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "Sugestao updated successfully"})

    @classmethod
    def get(cls, id_sugestao):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sugestao WHERE id_sugestao = %s", (id_sugestao,))
            suggestion = cursor.fetchone()
            if suggestion:
                return JSONResponse(status_code=200, content={"id_sugestao": suggestion[0], "mensagem": suggestion[3]})
            raise HTTPException(status_code=404, detail="Sugestao not found")

class FeedbackIA(BaseModel):
    id_feedback: Optional[int]
    id_sugestao: int
    avaliacao: int
    comentario: Optional[str]
    data_feedback: Optional[datetime]

    @classmethod
    def create(cls, **kwargs):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO feedback_ia (id_sugestao, avaliacao, comentario)
                VALUES (%s, %s, %s) RETURNING id_feedback;
                """,
                (kwargs['id_sugestao'], kwargs['avaliacao'], kwargs.get('comentario'))
            )
            id_feedback = cursor.fetchone()[0]
            conn.commit()
            return JSONResponse(status_code=201, content={"id_feedback": id_feedback, **kwargs})

    @classmethod
    def delete(cls, id_feedback):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM feedback_ia WHERE id_feedback = %s", (id_feedback,))
            conn.commit()
            return JSONResponse(status_code=204)

    @classmethod
    def update(cls, id_feedback, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values())
        values.append(id_feedback)
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE feedback_ia SET {set_clause} WHERE id_feedback = %s", values)
            conn.commit()
            return JSONResponse(status_code=200, content={"message": "FeedbackIA updated successfully"})

    @classmethod
    def get(cls, id_feedback):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM feedback_ia WHERE id_feedback = %s", (id_feedback,))
            feedback = cursor.fetchone()
            if feedback:
                return JSONResponse(status_code=200, content={"id_feedback": feedback[0], "avaliacao": feedback[2], "comentario": feedback[3]})
            raise HTTPException(status_code=404, detail="FeedbackIA not found")
