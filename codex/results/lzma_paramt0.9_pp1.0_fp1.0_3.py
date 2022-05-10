from lzma import LZMADecompressor
LZMADecompressor().decompress(open('data.csv.xz', 'rb').read())

# load data
df = pd.read_csv('data.csv')

# add sub rows
df2 = pd.DataFrame()
for year in np.unique(df['Year'].values)[:-1]:
    temp = df[df['Year']==year]
    df2 = pd.concat([df2, temp], axis=0)
    df2 = pd.concat([df2, temp.iloc[-1:]], axis=0)
df = df2

# change name
df = df.replace(replace['name'])

# fix inf in death rate
for country in np.unique(df['country'].values):
    mask = (df['country'] == country)
    df.loc[mask, 'death_rate'] = np.nan
    df.loc[mask, 'death_rate'] = interpolate(df.loc[mask, 'death_rate'])

# interpolate death rate
df['death_rate'] = interpolate(df['death
