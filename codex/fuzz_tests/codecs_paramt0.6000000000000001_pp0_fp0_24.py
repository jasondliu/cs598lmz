import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def load_data(filename='data/train.csv'):
    df = pd.read_csv(filename, encoding='utf-8', errors='replace_with_space')
    df = df.dropna(how='any')
    df = df.drop(df[df['SentimentText'].str.len() < 2].index)
    return df

train = load_data()
train.head(10)

train.shape

def remove_stopwords(input_text):
    stopwords_list = stopwords.words('english')
    # Some words which might indicate a certain sentiment are kept via a whitelist
    whitelist = ["n't", "not", "no"]
    words = input_text.split() 
    clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1] 
    return " ".join(clean_words) 

def remove_mentions(input_text):

