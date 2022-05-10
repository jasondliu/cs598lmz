import codecs
codecs.register_error('replace_with_space', replacer)

def process_question(q, fields):
    
    # Remove some annoying characters.
    remove = [
        (u'\ufeff', u''),
        (u'\xa0', u' '),
    ]
    
    for k, v in remove:
        q = q.replace(k, v)
    
    # Turn a question into a set of tokens.
    tokens = [t.lower() for t in nltk.word_tokenize(q)]
    tokens = [t for t in tokens if len(t) > 1] # get rid of 1 letter words
    tokens = [t for t in tokens if not any(c.isdigit() for c in t)] # get rid of numbers
   
    # Stem each token.
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens_stemmed = map(lambda token: stemmer.stem(token), tokens)
    
    q = " ".join(tokens_stemmed)
    
    if q:
        fields
