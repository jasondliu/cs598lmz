import bz2
bz2.open('filename.bz2')

# gzip
import gzip
gzip.open('filename.gz')

# lzma
import lzma
lzma.open('filename.xz')
```

###### [Pandas](https://pandas.pydata.org/)

Used to work with tabular data. It is similar to SQL.

```python
import pandas as pd

# read CSV file
df = pd.read_csv('filename.csv')

# read JSON file
df = pd.read_json('filename.json')

# read Excel file
df = pd.read_excel('filename.xlsx')

# read HTML table
df = pd.read_html('html_table.html')

# read SQL database
df = pd.read_sql('select * from table_name', connection)

# select single column
df['column_name']

# select multiple column
df[['column_name1', 'column_name2']]

# select all rows
df
