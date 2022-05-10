import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start() # for Windows

#------------------------------------------ read data from csv file
df = pd.read_csv('data.csv', delimiter=',', parse_dates=['date'])

#------------------------------------------ data preprocessing
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.date
df['date'] = df['date'].astype(str)

df['summary'] = df['summary'].fillna('')
df['description'] = df['description'].fillna('')

df['text'] = df['summary'] + ' ' + df['description']

#------------------------------------------ use TFIDF
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(df['text'])

feature_names = tf.get_feature_names()

#------------------------------------------ get cosine similarity
# cosine_
