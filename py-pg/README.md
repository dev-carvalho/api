


## Ainda não foi testado!


- Certifique-se de ter instalado as dependências necessárias:
```bash
pip install psycopg2-binary fastapi uvicorn[standard] python-dotenv
```

<br>

- crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
```bash
POSTGRES_USER=<usuário_do_postgres>
POSTGRES_PASSWORD=<senha_do_postgres>
POSTGRES_HOST=<host_do_postgres>
POSTGRES_PORT=<porta_do_postgres>
POSTGRES_DB=<nome_do_banco_de_dados>
```
Lembre-se de substituir os valores entre < e > pelas suas informações do PostgreSQL.