import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = 'http://localhost:8000'; // Altere para a URL do seu servidor

export default function () {
    // Teste para usuários
    let usuario = {
        nome: "João Silva",
        email: "joao.silva@example.com",
        senha_hash: "hashed_password",
        data_criacao: new Date().toISOString()
    };
    check(http.post(`${BASE_URL}/usuarios/`, JSON.stringify(usuario), { headers: { 'Content-Type': 'application/json' } }), {
        'Usuário criado': (r) => r.status === 201,
    });

    let id_usuario = 1;
    check(http.get(`${BASE_URL}/usuarios/${id_usuario}`), {
        'Usuário obtido': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/usuarios/${id_usuario}`, JSON.stringify(usuario), { headers: { 'Content-Type': 'application/json' } }), {
        'Usuário atualizado': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/usuarios/${id_usuario}`), {
        'Usuário deletado': (r) => r.status === 204,
    });

    // Teste para categorias
    let categoria = {
        nome: "Saúde",
        cor: "#FF5733"
    };
    check(http.post(`${BASE_URL}/categorias/`, JSON.stringify(categoria), { headers: { 'Content-Type': 'application/json' } }), {
        'Categoria criada': (r) => r.status === 201,
    });

    let id_categoria = 1;
    check(http.get(`${BASE_URL}/categorias/${id_categoria}`), {
        'Categoria obtida': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/categorias/${id_categoria}`, JSON.stringify(categoria), { headers: { 'Content-Type': 'application/json' } }), {
        'Categoria atualizada': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/categorias/${id_categoria}`), {
        'Categoria deletada': (r) => r.status === 204,
    });

    // Teste para hábitos
    let habito = {
        id_usuario: 1,
        id_categoria: 1,
        nome: "Exercício",
        descricao: "Fazer exercícios físicos diariamente",
        meta: 30,
        unidade: "minutos",
        recorrencia: "diario",
        ativo: true,
        data_criacao: new Date().toISOString()
    };
    check(http.post(`${BASE_URL}/habitos/`, JSON.stringify(habito), { headers: { 'Content-Type': 'application/json' } }), {
        'Hábito criado': (r) => r.status === 201,
    });

    let id_habito = 1;
    check(http.get(`${BASE_URL}/habitos/${id_habito}`), {
        'Hábito obtido': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/habitos/${id_habito}`, JSON.stringify(habito), { headers: { 'Content-Type': 'application/json' } }), {
        'Hábito atualizado': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/habitos/${id_habito}`), {
        'Hábito deletado': (r) => r.status === 204,
    });

    // Teste para frequências
    let frequencia = {
        id_habito: 1,
        data: new Date().toISOString(),
        progresso: 15,
        concluido: false
    };
    check(http.post(`${BASE_URL}/frequencias/`, JSON.stringify(frequencia), { headers: { 'Content-Type': 'application/json' } }), {
        'Frequência criada': (r) => r.status === 201,
    });

    let id_frequencia = 1;
    check(http.get(`${BASE_URL}/frequencias/${id_frequencia}`), {
        'Frequência obtida': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/frequencias/${id_frequencia}`, JSON.stringify(frequencia), { headers: { 'Content-Type': 'application/json' } }), {
        'Frequência atualizada': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/frequencias/${id_frequencia}`), {
        'Frequência deletada': (r) => r.status === 204,
    });

    // Teste para notificações
    let notificacao = {
        id_habito: 1,
        horario: new Date().toISOString(),
        mensagem: "Hora de cumprir seu hábito!",
        ativo: true
    };
    check(http.post(`${BASE_URL}/notificacoes/`, JSON.stringify(notificacao), { headers: { 'Content-Type': 'application/json' } }), {
        'Notificação criada': (r) => r.status === 201,
    });

    let id_notificacao = 1;
    check(http.get(`${BASE_URL}/notificacoes/${id_notificacao}`), {
        'Notificação obtida': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/notificacoes/${id_notificacao}`, JSON.stringify(notificacao), { headers: { 'Content-Type': 'application/json' } }), {
        'Notificação atualizada': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/notificacoes/${id_notificacao}`), {
        'Notificação deletada': (r) => r.status === 204,
    });

    // Teste para objetivos
    let objetivo = {
        id_usuario: 1,
        descricao: "Perder peso",
        prioridade: "media", // Use um valor válido do enum
        status: "ativo", // Use um valor válido do enum
        data_criacao: new Date().toISOString()
    };
    check(http.post(`${BASE_URL}/objetivos/`, JSON.stringify(objetivo), { headers: { 'Content-Type': 'application/json' } }), {
        'Objetivo criado': (r) => r.status === 201,
    });

    let id_objetivo = 1;
    check(http.get(`${BASE_URL}/objetivos/${id_objetivo}`), {
        'Objetivo obtido': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/objetivos/${id_objetivo}`, JSON.stringify(objetivo), { headers: { 'Content-Type': 'application/json' } }), {
        'Objetivo atualizado': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/objetivos/${id_objetivo}`), {
        'Objetivo deletado': (r) => r.status === 204,
    });

    // Teste para dados do usuário
    let dados_usuario = {
        id_usuario: 1,
        idade: 30,
        peso: 70.5,
        altura: 1.75,
        condicoes_saude: "Nenhuma",
        preferencias: "Vegetariano"
    };
    check(http.post(`${BASE_URL}/dados_usuario/`, JSON.stringify(dados_usuario), { headers: { 'Content-Type': 'application/json' } }), {
        'Dados do usuário criados': (r) => r.status === 201,
    });

    let id_dados_usuario = 1;
    check(http.get(`${BASE_URL}/dados_usuario/${id_dados_usuario}`), {
        'Dados do usuário obtidos': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/dados_usuario/${id_dados_usuario}`, JSON.stringify(dados_usuario), { headers: { 'Content-Type': 'application/json' } }), {
        'Dados do usuário atualizados': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/dados_usuario/${id_dados_usuario}`), {
        'Dados do usuário deletados': (r) => r.status === 204,
    });

    // Teste para sugestões
    let sugestao = {
        id_usuario: 1,
        tipo: "sugestao_tipo_exemplo", // Use um valor válido do enum
        mensagem: "Sugestão para melhorar o aplicativo",
        data_sugestao: new Date().toISOString(),
        aceita: false
    };
    check(http.post(`${BASE_URL}/sugestoes/`, JSON.stringify(sugestao), { headers: { 'Content-Type': 'application/json' } }), {
        'Sugestão criada': (r) => r.status === 201,
    });

    let id_sugestao = 1;
    check(http.get(`${BASE_URL}/sugestoes/${id_sugestao}`), {
        'Sugestão obtida': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/sugestoes/${id_sugestao}`, JSON.stringify(sugestao), { headers: { 'Content-Type': 'application/json' } }), {
        'Sugestão atualizada': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/sugestoes/${id_sugestao}`), {
        'Sugestão deletada': (r) => r.status === 204,
    });

    // Teste para feedback
    let feedback = {
        id_sugestao: 1,
        avaliacao: 5,
        comentario: "Ótima sugestão!",
        data_feedback: new Date().toISOString()
    };
    check(http.post(`${BASE_URL}/feedbacks/`, JSON.stringify(feedback), { headers: { 'Content-Type': 'application/json' } }), {
        'Feedback criado': (r) => r.status === 201,
    });

    let id_feedback = 1;
    check(http.get(`${BASE_URL}/feedbacks/${id_feedback}`), {
        'Feedback obtido': (r) => r.status === 200,
    });

    check(http.put(`${BASE_URL}/feedbacks/${id_feedback}`, JSON.stringify(feedback), { headers: { 'Content-Type': 'application/json' } }), {
        'Feedback atualizado': (r) => r.status === 200,
    });

    check(http.delete(`${BASE_URL}/feedbacks/${id_feedback}`), {
        'Feedback deletado': (r) => r.status === 204,
    });

    sleep(1); // Pausa entre as requisições
}
