# README - Teste do Endpoint e Performance com K6

Este repositório contém um script de teste do endpoint de teste e performance utilizando o K6, uma ferramenta de código aberto para testes de carga e performance. O script realiza operações CRUD (Criar, Ler, Atualizar, Deletar) em várias entidades, como usuários, categorias, hábitos, frequências, notificações, objetivos, dados do usuário, sugestões e feedbacks.

## Pré-requisitos

É recomendável limpar o banco de dados antes com um:
    bash```
    docker compose down --volumes
    ```

Antes de executar o script, você precisa ter o K6 instalado em sua máquina. Você pode instalar o K6 seguindo as instruções na [documentação oficial do K6](https://k6.io/docs/getting-started/installation/).

## Configuração

**Altere a URL base**:
   No arquivo `k6/script_teste.js`, altere a constante `BASE_URL` para a URL do seu servidor:
   ```javascript
   const BASE_URL = 'http://localhost:8000'; // Altere para a URL do seu servidor
   ```

## Execução do Script

Para executar o script, utilize o seguinte comando no terminal:
```bash
k6 run k6/script_teste.js
```

## Estrutura do Script

O script realiza os seguintes testes:

- **Usuários**: Criação, obtenção, atualização e deleção de usuários.
- **Categorias**: Criação, obtenção, atualização e deleção de categorias.
- **Hábitos**: Criação, obtenção, atualização e deleção de hábitos.
- **Frequências**: Criação, obtenção, atualização e deleção de frequências.
- **Notificações**: Criação, obtenção, atualização e deleção de notificações.
- **Objetivos**: Criação, obtenção, atualização e deleção de objetivos.
- **Dados do Usuário**: Criação, obtenção, atualização e deleção de dados do usuário.
- **Sugestões**: Criação, obtenção, atualização e deleção de sugestões.
- **Feedback**: Criação, obtenção, atualização e deleção de feedbacks.

Cada operação é verificada com um `check` para garantir que a resposta do servidor esteja correta (status HTTP esperado).

## Considerações Finais

Certifique-se de que seu servidor esteja em execução antes de executar os testes. O K6 irá simular requisições para o seu servidor e você poderá monitorar o desempenho e a resposta do sistema.

Para mais informações sobre como usar o K6, consulte a [documentação oficial do K6](https://k6.io/docs/).
