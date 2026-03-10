from core.logging_config import init_logger
from db.connection import psql_connection_test, psql_connection
from db.repository import insert_member, select_ids
from run_schema import run_migrations
import logging
from ingestion.get_data import get_selfdev_members
from load.load import load_loaded_at
from transform.transform_data import validate_empty

def main():
    init_logger()
    psql_connection_test()
    conn = psql_connection()
    
    try:
        # run_migrations(conn)
    
        members = get_selfdev_members('data/raw/data.json')
        
        print(validate_empty(members)[1])
        # for member in members:
        #     insert_member(conn, member)
            
        
        # logging.info("Members inserted")
        # conn.commit()   
        
        # load_loaded_at(conn)
        
        # logging.info("Loaded_at values inserted")
        # conn.commit()       
    except Exception as e:
        conn.rollback()
        logging.error(f"Pipeline failed: {e}") 

    finally:
        conn.close()


if __name__ == '__main__':
    main()