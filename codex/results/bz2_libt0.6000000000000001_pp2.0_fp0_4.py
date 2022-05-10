import bz2
bz2.BZ2File('data/titles-enwiki-latest.bz2')

# column_names = ['title', 'body']
# df = pd.read_csv('data/titles-enwiki-latest.bz2', sep='\t', names=column_names, compression='bz2')
# df.head()

# df.shape

# df.columns

# df.info()

# df.body.describe()

# df.body.value_counts()

# df.body.isnull()

# df.body.notnull()

# df.body[df.body.notnull()]

# df.body.dropna()

# df.body.fillna(0)

# df.body.fillna('MISSING')

# df.body.dtype

# df.body.astype(str)

# df.body.astype(float)

# df.body.astype(bool)

# df.body.astype(int)

# df
