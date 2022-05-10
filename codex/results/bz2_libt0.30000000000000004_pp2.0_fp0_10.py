import bz2
bz2.BZ2File(path, 'r')

# Reading in a pickle
import pickle
with open(path, 'rb') as file:
    data = pickle.load(file)

# Reading Microsoft Excel files
import pandas as pd
xlsx = pd.ExcelFile(path)
table = xlsx.parse('Sheet1')

# Interacting with HTML and Web APIs
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
data = resp.json()
data[0]['title']

# Interacting with Databases
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""
con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida',
