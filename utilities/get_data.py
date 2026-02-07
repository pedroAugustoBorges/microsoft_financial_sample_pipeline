import json
import logging
from utilities.helper_psql import insert_member

def get_selfdev_members(psql_conn):
    with open('data/raw/data.json') as json_file:
        data = json.load(json_file)
        
        for members in data:
            for member in data[members]:
                print(f'Processing member {member['name']}')
                insert_member(psql_conn, member)
                
            
            