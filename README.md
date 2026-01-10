Uma API de gerenciamento de tarefas construida com **FLASK** e **SQLite**, com suporte completo
ao **CRUD** (create, read, update, delete).

## Tecnologias utilizadas

- Python version 3.x.x
- Flask
- Flask alchemy
- SQLite

## Rotas disponiveis

### 1. GET /tasks
- Lista todas as tarefas
- Exemplo de resposta:

[
  {
    "id": 1,
    "title": "Estudar Flask",
    "done": false
  }
]

### 2. POST /tasks
- Cria uma nova tarefa
- Exemplo de resposta:

{
  "id": 2,
  "title": "Nova tarefa",
  "done": false
}

### 3. PUT /task/<id>
- atualiza uma tarefa existente
- exemplo de resposta

{
    "id": 1,
    "title": "tarefa atualizada"
    "done": true
}

### 4. DELETE /task/<id>
- deleta a tarefa oelo ID
- exemplo de requisição e de retorno

DELETE http://localhost:5000/tasks/1
######################
{
    "message": "Tarefa deletada"
}

## Como rodar o projeto?
## 1. Clone o repositorio:
git clone <URL_DO_SEU_REPOSITORIO>
cd TASK_MANAGER_API

## 2. Crie e ative o ambiente virtual:
python -m venv venv
# win
venv\scripts\activate
# mac/linux
source venv/bin/activate

## 3. instale as dependencias:
pip install -r requirements.txt

## 4. e rode o seu servidor :D
python app.py

A API estará disponivel em http://localhost:5000/

## Testando a API 
use o thunder client ou o postman para enviar requisiçoes
teste get, post, put e delete conforme eu ensinei acima
sempre envie o json correto para POST e PUT

## Minhas observações
O banco de dados usado é o SQLite, entao, todas as alterações sao salvas localmente no arquivo tasks.db
as tarefas sao indentificadas pelo campo id, que é incremental e unico
para garantir que seus testes fiquem limpos, voce pode apagar o arquivo task.db e tentar denovo :D