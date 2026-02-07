import psycopg2
import logging
from rich.logging import RichHandler
 

import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

def init_logger():
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s = %(message)s',
                        handlers= [logging.FileHandler('log.log'),
                                   logging.StreamHandler()],
                        )
    logging.info('Start of program and logger')

def psql_connection_test():
    
    conn = None
    
    try:
        
        logging.info('Connecting to the PostgreeSQL database')
        
        conn = psycopg2.connect(
            host = POSTGRES_HOST,
            database = POSTGRES_DB,
            user = POSTGRES_USER,
            password = POSTGRES_PASSWORD,
            port = POSTGRES_PORT
            )
        
        cur = conn.cursor()
        
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        
        logging.info(db_version)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    
    finally:
        if conn is not None:
            conn.close()
            logging.info('Database connection closed')
            
    
def psql_connection():
    conn = None
    
    try:
        logging.info('Connecting to the PostgreSQL database')
        conn = conn = psycopg2.connect(
            host = POSTGRES_HOST,
            database = POSTGRES_DB,
            user = POSTGRES_USER,
            password = POSTGRES_PASSWORD,
            port = POSTGRES_PORT
            )
        
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)


def create_table(psql_conn):
    q_create_table = """
    CREATE TABLE IF NOT EXISTS members(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        discord_id VARCHAR(255) NOT NULL,
        coding_motivation VARCHAR(255) NOT NULL
    )
    """
    
    try:
        cur = psql_conn.cursor()
        
        cur.execute(q_create_table)
        
        logging.info(f"Executed query {q_create_table}")
        
        cur.close()
        
        psql_conn.commit()
        
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        

def insert_member(psql_conn, member):
    q_insert_member ="""
    INSERT INTO members (name, discord_id, coding_motivation)
    VALUES (%s, %s, %s)
    """
    
    try: 
        cur = psql_conn.cursor()
        
        cur.execute(q_insert_member, (member['name'], member['discord_name'], member['reason_to_code']))
        
        psql_conn.commit()
    
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(error)