from bz2 import BZ2Decompressor
BZ2Decompressor()

from pitchfork import lda_model, count_vectorizer, tfidf_transformer
from pitchfork.lda_model import ldamodel
from pitchfork.count_vectorizer import countvec
from pitchfork.tfidf_transformer import tfidf
from pitchfork.lda_preprocessing import stopwords

from gensim import corpora, models, matutils
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora.dictionary import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from gensim.matutils import Sparse2Corpus
import pyLDAvis.gensim

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as nltk_stopwords


