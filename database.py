import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\Usuario\Desktop\Projetos Python\.env")

conexao = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conexao.cursor()

def buscar_do_banco(tabela):
    cursor.execute(f"SELECT * FROM {tabela}")
    colunas = [desc[0] for desc in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]
