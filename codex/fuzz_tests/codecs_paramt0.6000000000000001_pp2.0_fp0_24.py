import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# create a tokenizer that ignores punctuation and converts everything to lower case
tokenizer = RegexpTokenizer(r'\w+')

# create stemmer
porter = PorterStemmer()

# create lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# create stop words list
stop_words = set(stopwords.words('english'))

# add words to stop words list
stop_words.add('http')
stop_words.add('https')
stop_words.add('twitter')
stop_words.add('com')
stop_words.add('tweet')
stop_words.add('retweet')
stop_words.add('tweets')
stop_words.add('retweets')
stop_words.add('rt')
stop_words.add('amp')
stop_words.add('via')
stop_words.add('u2026')
stop_words.add('youtu')
stop_words.add('be')
stop_words
