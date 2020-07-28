# Petshop (Com Autenticação)

Esta é uma aplicação feita em Django que oferecendo um CRUD de Pets, simulando um Petshop Canino bem simples.
A diferença deste projeto para o anterior feito em django com o mesmo tema, é que este tem a necessidade de autenticação para acessar todas as rotas normais (exceto a de login/adquirir token de autenticação).

Como Executar

Siga a lista de comandos abaixo para organizar todas as necessidades e fazer com que a aplicação execute.
Obs.: Este projeto foi criado utilizando o python 3.8. Sugiro que o utilize para evitar conflitos que possam acontecer a partir do versionamento dos pacotes.
<ol>
  <li>Crie o ambiente virtual do projeto: python3 -m venv venv</li>
  <li>Ative-o: source venv/bin/activate</li>
  <li>Instale suas dependências: pip3 install -r requirements.txt</li>
  <li>Crie o banco de dados executando as migrations: python3 manage.py migrate</li>
  <li>Crie um usuário primário: python3 manage.py createsuperuser</li>
  <li>Inicie o Servidor: python3 manage.py runserver</li>
</ol>

E pronto, a aplicação estará executando de forma local na porta 8000.

<h2>Objetos</h2>

Na aplicação, os Pets seguem o seguinte modelo de objeto, tanto na adição quanto no retorno do mesmo:</br>
```json
{
  "id": "Presente somente no retorno das requisições GET, PUT e POST.",
  "nome": "Nome do pet. Obrigatório.",
  "raca": "A raça do pet. Utiliza de um dos tipos descritos abaixo. Obrigatório",
  "idade": "A idade do pet. Facultativo."
}
```

Opções na inserção de raças (choices):</br>
```json
[
  "LAB", // Labrador
  "BUL", // Boldogue
  "POO", // Poodle
  "PAS", // Pastor Alemão
  "BEA", // Beagle
  "GOL", // Golden Retriever
  "CHI", // Chihuahua
  "HUS"  // Husky Siberiano
]
```

Objeto necessário na rota de autenticação para recuperação do token do usuario a autenticar:</br>
```json
{
  "username": "nome de usuario",
  "password": "senha do usuario"
}
```

Objeto de retorno ao autenticar-se com as credenciais:</br>
```json
{
  "auth_token": "token do usuário",
  "user": {
    "id": "id do usuário",
    "nome": "nome do usuário"
  },
  "created": "data de criação do usuário"
}
```

<h2>Requisições</h2>

<p>Abaixo está uma tabela de requisições em relação aos pets.</p>

| Método | URL                 | Descrição                                    |
|--------|---------------------|----------------------------------------------|
| GET    | /api/core/pets      | Retorna todos os pets.                       |
| GET    | /api/core/pets/:id  | Retorna um único pet com o id fornecido.     |
| POST   | /api/core/pets      | Adiciona um pet seguindo o modelo de objeto. |
| PUT    | /api/core/pets/:id  | Altera um pet de acordo com o id fornecido.  |
| DELETE | /api/core/pets/:id  | Deleta um pet de acordo com o id fornecido.  |

<p>Abaixo está uma tabela com uma única requisição atrelada à autenticação.</p>

| Método | URL                 | Descrição                                                          |
|--------|---------------------|--------------------------------------------------------------------|
| POST   | /api/core/login      | Traz as informações do usuário, incluindo o token de autenticação. |