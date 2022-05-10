import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%
# Read data
df = pd.read_csv('../data/raw/data.csv', sep=';', decimal=',')

#%%
# Data cleaning
df.drop(columns=['Unnamed: 0'], inplace=True)
df.rename(columns={'Unnamed: 0.1': 'id'}, inplace=True)
df.drop(columns=['id'], inplace=True)
df.drop(columns=['Unnamed: 0.1.1'], inplace=True)
df.drop(columns=['Unnamed: 0.1.1.1'], inplace=True)
df.drop(columns=['Unnamed: 0.1.1.1.1'], inplace=True)
df.drop(columns=['Unnamed: 0.1.1.1.1.1'], inplace=True)
df.drop(columns=['Unnamed: 0.
