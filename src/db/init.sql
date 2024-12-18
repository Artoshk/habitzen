-- Tabela de Usuários
CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Categorias
CREATE TABLE categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    cor VARCHAR(7) DEFAULT '#FFFFFF' -- Hexadecimal para cores
);

CREATE TYPE recorrencia_enum AS ENUM ('diario', 'semanal', 'mensal');

-- Tabela de Hábitos
CREATE TABLE habito (
    id_habito SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_categoria INT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    meta INT DEFAULT 1, -- Meta diária, como "beber 2L de água"
    unidade VARCHAR(20) DEFAULT 'vezes', -- Ex: "vezes", "minutos", "litros"
    recorrencia recorrencia_enum DEFAULT 'diario',
    ativo BOOLEAN DEFAULT TRUE,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
);

-- Tabela de Frequências
CREATE TABLE frequencia (
    id_frequencia SERIAL PRIMARY KEY,
    id_habito INT NOT NULL,
    data DATE NOT NULL,
    progresso INT DEFAULT 0, -- Quantidade registrada no dia
    concluido BOOLEAN DEFAULT FALSE, -- Se a meta foi atingida
    FOREIGN KEY (id_habito) REFERENCES habito (id_habito),
    UNIQUE (id_habito, data) -- Evitar registros duplicados para o mesmo dia
);

-- Tabela de Notificações
CREATE TABLE nofificacao (
    id_notificacao SERIAL PRIMARY KEY,
    id_habito INT NOT NULL,
    horario TIME NOT NULL, -- Horário para o lembrete
    mensagem VARCHAR(255) DEFAULT 'Hora de cumprir seu hábito!',
    ativo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_habito) REFERENCES habito (id_habito)
);

CREATE TYPE objetivo_prioridade_enum AS ENUM('alta', 'media', 'baixa');
CREATE TYPE objetivo_status_enum AS ENUM('ativo', 'concluido', 'cancelado');

CREATE TABLE objetivo (
    id_objetivo SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    descricao TEXT NOT NULL,
    prioridade objetivo_prioridade_enum DEFAULT 'media',
    status objetivo_status_enum DEFAULT 'ativo',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE dados_usuario (
    id_usuario INT PRIMARY KEY,
    idade INT,
    peso DECIMAL(5, 2), -- Para cálculos de saúde (ex: IMC)
    altura DECIMAL(4, 2),
    condicoes_saude TEXT, -- Ex: "diabetes, hipertensão"
    preferencias TEXT, -- Ex: "caminhada, yoga"
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TYPE sugestao_tipo_enum AS ENUM('novo_habito', 'melhoria', 'alerta');

CREATE TABLE sugestao (
    id_sugestao SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    tipo sugestao_tipo_enum NOT NULL, -- Tipo da sugestão
    mensagem TEXT NOT NULL, -- Mensagem gerada pela IA
    data_sugestao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    aceita BOOLEAN DEFAULT NULL, -- NULL enquanto não respondido pelo usuário
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE feedback_ia (
    id_feedback SERIAL PRIMARY KEY,
    id_sugestao INT NOT NULL,
    avaliacao INT CHECK (avaliacao BETWEEN 1 AND 5), -- Nota de 1 a 5
    comentario TEXT, -- Comentário opcional do usuário
    data_feedback TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_sugestao) REFERENCES sugestao (id_sugestao)
);