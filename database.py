import psycopg2
import os

conexao = psycopg2.connect(
    host="localhost",
    database="busca_eletronicos",
    user="postgres",
    password="Fe26122005"
)

cursor = conexao.cursor()

def buscar_do_banco(tabela):
    cursor.execute(f"SELECT * FROM {tabela}")
    colunas = [desc[0] for desc in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]