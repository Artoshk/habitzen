from enum import Enum

# Enums
class RecorrenciaEnum(str, Enum):
    diario = "diario"
    semanal = "semanal"
    mensal = "mensal"

class ObjetivoPrioridadeEnum(str, Enum):
    alta = "alta"
    media = "media"
    baixa = "baixa"

class ObjetivoStatusEnum(str, Enum):
    ativo = "ativo"
    concluido = "concluido"
    cancelado = "cancelado"

class SugestaoTipoEnum(str, Enum):
    novo_habito = "novo_habito"
    melhoria = "melhoria"
    alerta = "alerta"