import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('ignore'))

# read file
with codecs.open('./data/train.tsv', 'r', encoding='utf8', errors='replace_with_space') as f:
    data = [line.strip().split('\t') for line in f.readlines()]
    data = pd.DataFrame(data[1:], columns=data[0])

# preprocess data
# stopwords = nltk.corpus.stopwords.words('english')
# data['Sentence'] = data['Sentence'].apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords]))

# split data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# build vocabulary
vocab = set()
for i, sentence in enumerate(train_data['Sentence']):
    vocab.update(sentence.split())

# build word2idx
