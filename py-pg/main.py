#
# Código gerado pelo GTP em 24/03/2023
# 
# escreva um codigo comentado para  GRUP para postgres no padrão API REST em Pythom utilizando FastAPI
#

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import DictCursor
from typing import List

# Define o modelo dos usuários
class User(BaseModel):
    id: int
    name: str
    email: str

# Cria uma conexão com o PostgreSQL
def get_conn():
    conn = psycopg2.connect(
        dbname = f"{os.getenv('POSTGRES_DB')}",
        user = f"{os.getenv('POSTGRES_USER')}",
        password = f"{os.getenv('POSTGRES_PASSWORD')}",
        host = f"{os.getenv('POSTGRES_HOST')}",
        port = f"{os.getenv('POSTGRES_PORT')}",
        cursor_factory=DictCursor
    )
    return conn

# Inicializa o objeto FastAPI
app = FastAPI()

# Define as rotas da API
@app.get("/users", response_model=List[User])
def read_users():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        return rows

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return row

@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, name, email",
                    (user.name, user.email))
        row = cur.fetchone()
        conn.commit()
        return row

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING id, name, email",
                    (user.name, user.email, user_id))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        conn.commit()
        return row

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
