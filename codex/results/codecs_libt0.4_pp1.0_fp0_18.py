import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Create a list of stopwords to be removed from tweets.
stoplist = set('for a of the and to in on'.split(' '))

# Create a list of punctuation marks to be removed from tweets.
punctuation = list(string.punctuation)

# Create a list of stopwords to be removed from tweets.
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', 'I', 'I\'m', 'I\'ve', 'I\'d', 'I\'ll', 'I’m', 'I’ve', 'I’d', 'I’ll']

# Create a list of emojis to be removed from tweets.
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F
