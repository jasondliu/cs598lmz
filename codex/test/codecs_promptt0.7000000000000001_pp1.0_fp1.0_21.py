import codecs
# Test codecs.register_error('replace_with_space', partial(codecs.replace_errors, ' '))
# codecs.register_error('replace_with_space', partial(codecs.replace_errors, ' '))

# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

# from sklearn.feature_extraction.text import CountVectorizer
