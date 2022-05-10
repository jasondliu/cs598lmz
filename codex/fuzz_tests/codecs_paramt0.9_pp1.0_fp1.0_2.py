import codecs
codecs.register_error('replace_with_space', codecs.replace_with
                      (' ', ' '))


from gensim.parsing import strip_punctuation, strip_numeric, strip_tags, stem_text
from copy import copy as copy_
from nltk.stem.porter import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


pd.set_option('display.float_format', lambda x: '%.2f' % x)

from scipy.sparse import coo
from gensim.models import Word2Vec
from gensim.corpora import Dictionary
from gensim.models.tfidfmodel import TfidfModel
from sklearn.preprocessing import scale
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
# from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer
import nltk
nltk.download('stopwords')

# from sk
