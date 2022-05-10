import bz2
bz2.BZ2File('class.txt.bz2')

# UTF-8
import chardet
with open('class.txt') as f:
    data = f.read()
    chardet.detect(data)

with open('class.txt', encoding='utf-8') as f:
    data = f.read()
    chardet.detect(data)

# Pandas
import pandas as pd
df = pd.read_csv('class.txt', sep='\t')
df = pd.read_csv('class.txt', sep='\t', encoding='utf-8')
df.head()

# Write file
df.to_csv('class_refactored.txt', sep='\t', index=False, encoding='utf-8')

# Check
df2 = pd.read_csv('class_refactored.txt', sep='\t')
df.head()
df2.head()

# Pickle
import pickle
with open('class_pickle.txt', 'wb') as f:
   
