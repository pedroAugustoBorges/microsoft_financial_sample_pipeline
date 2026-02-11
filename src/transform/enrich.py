import pandas as pd
from extract.extract_json import extract_data
from ingestion.create_mock_date import random_date

data = extract_data()


datas_random= pd.Series(random_date(limit = len(data)))

data['datetime_random'] = datas_random

print(data)