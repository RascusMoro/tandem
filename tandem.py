import random
from sqlite3 import dbapi2
import pandas as pd

db = pd.read_csv('tandem_db.csv', delimiter=',')
