import codecs
codecs.open(filename, 'r', encoding='utf-8')

import csv

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv

with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

import os

os.getcwd()
os.chdir('/Users/thomas/Documents')
os.listdir()

os.path.join('tmp', 'data', os.listdir()[0])

import pandas as pd

df = pd.read_csv(filename)
df

import pandas as pd

df = pd.read_csv(filename, index_col=0, parse_dates=True)
df

df.head()
df.tail()
df.index
df.columns
df.values
df.T
df.sort_index(axis=1, ascending=False)

