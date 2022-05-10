import codecs
codecs.register_error('surrogate_or_unknown', ErrorHandler)

#Import the data for the analysis
df = pd.read_csv('/home/ekim_reverse/PyCode/study/Python.Study.Code/project/[0]data/[1]data_collection/[2]data_collection_sample.csv', encoding='utf-8', index_col=None)
#Filter the source only from twitter
df['source'] = df['source'].str.split(">").str[1].str.split("<").str.get(0)
df = df.loc[df['source'] == 'Twitter for iPhone']
df = df[['id', 'text', 'retweet_count', 'created_at']]
#Sort the data by time
df = df.sort_values(['created_at'], ascending=[True])

#Create the list of dates
df['created_at'] = pd.to_datetime(df['created_at'])
df['date'] = df['created_at'].dt.date
list_date = []
list_date = df['date'
