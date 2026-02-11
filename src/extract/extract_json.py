import pandas as pd
import logging
import os
import json 

PATH = 'data/raw/data.json'

def check_file(path):
    if os.path.isfile(path):
        return True
    else:
        return False
        

def extract_data(path = PATH):
    if check_file:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            
            if isinstance(data, dict) and 'selfdev_members' in data:
                return pd.json_normalize(data, record_path=['selfdev_members'])
            
            if isinstance(data, list):
                return pd.read_json(data) 
    
    else:
        logging.error(f'Error while extract. {path} is not a file')
        





