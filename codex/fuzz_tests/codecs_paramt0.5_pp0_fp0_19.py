import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Define some global variables

# A mapping from a language to a list of language-specific stopwords
lang_stopwords = {'en': stopwords.words('english'),
                  'es': stopwords.words('spanish'),
                  'fr': stopwords.words('french'),
                  'it': stopwords.words('italian'),
                  'de': stopwords.words('german'),
                  'nl': stopwords.words('dutch')}

# A mapping from a language to a stemmer
lang_stemmer = {'en': SnowballStemmer('english'),
                'es': SnowballStemmer('spanish'),
                'fr': SnowballStemmer('french'),
                'it': SnowballStemmer('italian'),
                'de': SnowballStemmer('german'),
                'nl': SnowballStemmer('dutch')}

# A mapping from a language to a lemmatizer
lang_lemmatizer = {'en': WordNetLemmat
