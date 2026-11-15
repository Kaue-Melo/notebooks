import pandas as pd
from sqlalchemy import create_engine

db_config = {
    'user': 'your_username',
    'pwd': 'your_password',
    'host': 'localhost',
    'port': 5432,
    'db': 'your_database'
}

DELETE FROM table_name WHERE ANO_EGRESO = 2023
