import psycopg2
import logging
from psycopg2.extras import execute_values

def insert_member(psql_conn, member):
    query = """
    INSERT INTO MEMBERS(name, discord_id, motivation_member)
    VALUES(%s, %s, %s)
    ON CONFLICT(discord_id)
    DO UPDATE SET   
    name = EXCLUDED.name,
    motivation_member = EXCLUDED.motivation_member
    """
    

    try:
        with psql_conn.cursor() as curr:
            curr = psql_conn.cursor()
        
            curr.execute(query, (member['name'], member['discord_name'], member['reason_to_code']))
    
        
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error while inserting member {member} - {error}")
        

def insert_loaded_at(psql_conn, data):
    
    insert_dates = """
    UPDATE members
    SET datetime_created = data.datetime_created
    FROM (VALUES %s) AS data(datetime_created, id)
    WHERE members.id = data.id
    """
    
    try:
        
        with psql_conn.cursor() as curr:
            execute_values(curr, insert_dates, data)
        
    except(Exception, psycopg2.DatabaseError) as e:
        logging.error("Error while insert loaded_at in datetime_created")
        
        
    
    
def select_ids(psql_conn):
    query = """
    SELECT id
    FROM members
    WHERE members.datetime_created is NULL
    """
    
    with psql_conn.cursor() as curr:
        curr.execute(query)
        
        return [row[0] for row in curr.fetchall()]
        
        