import bz2
bz2_file = bz2.BZ2File('./data/test.json.bz2')
for line in bz2_file:
    print(line)
    break

import json
records = [json.loads(line) for line in bz2_file]
records[0]
records[0]['title']

import pandas as pd
df = pd.DataFrame(records)
df

df.info()

df['title']

df['title'][0]

df.title

df['title'][0]

df.title[0]

df[['title','year']]

df.columns

df.dtypes

df.get_dtype_counts()

df.columns

df.year

df.year.astype(str)

df.year.astype(str).str.contains('1995')

df[df.year.astype(str).str.contains('1995')]

df[df.year.astype(str).
