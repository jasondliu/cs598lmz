import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])
tokenizer = PunktSentenceTokenizer(punkt_param)

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

from nltk.stem.wordnet import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

from nltk.corpus import wordnet as wn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from gensim import corpora, models, similarities

from sklearn.feature_ext
