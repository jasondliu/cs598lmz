import lzma
lzma.decompress(open(url, 'rb').read()).decode('utf-8')

import re
re.sub(r'[^\w\s]','',data)

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# removing the stop words
stop_words = set(stopwords.words('english'))
stop_words.remove('no')
stop_words.remove('not')

# word tokenization
tokens = word_tokenize(data)

# removing the stop words
filtered_sentence = [w for w in tokens if not w in stop_words]

# stemming
ps = PorterStemmer()
stemmed_sentence = [ps.stem(w) for w in filtered_sentence]

# lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_sentence
