import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

conn = psycopg2.connect(
    host = POSTGRES_HOST,
    database = POSTGRES_DB,
    user = POSTGRES_USER,
    password = POSTGRES_PASSWORD,
    port = '5432'
)

conn.autocommit = True 
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS TEST (id SERIAL PRIMARY KEY, nome VARCHAR(10), product VARCHAR(1))')

cur.close()
conn.close()