import random
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

MIN_YEAR = 2023
max_year = datetime.now().year

def start_date(min_year = MIN_YEAR):
    return datetime(min_year, 1, 1, 00, 00, 00)

def end_date(start_time):
    years = (max_year - MIN_YEAR + 1)
    return start_time + timedelta(days = 365 * years)


# def random_date(limit):
#     start = start_date()
#     end = end_date(start)
#     dates = []
#     for i in range(0, limit):
#         random_date = start + (end-start) * random.random()
#         dates.append(random_date.strftime('%Y-%m-%d'))
#     return dates


def random_date(limit):
    start = start_date()
    end = end_date(start)
    
    return np.random.choice(pd.date_range(start= start, end = end), size = limit)