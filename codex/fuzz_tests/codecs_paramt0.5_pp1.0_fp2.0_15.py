import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load data
df = pd.read_csv('data/train.csv')

# Add columns for the length of the text
df['txtlen'] = df['text'].apply(lambda x: len(x))

# Add columns for the number of words in the text
df['numwords'] = df['text'].apply(lambda x: len(x.split()))

# Add columns for the number of unique words in the text
df['numunique'] = df['text'].apply(lambda x: len(set(x.split())))

# Add columns for the number of characters in the text
df['numchars'] = df['text'].apply(lambda x: len(x.replace(' ', '')))

# Add columns for the number of stopwords in the text
df['numstopwords'] = df['text'].apply(lambda x: len([w for w in x.lower().split() if w in stopwords.words('english')]))

# Add columns for the number of punctuations in the text
