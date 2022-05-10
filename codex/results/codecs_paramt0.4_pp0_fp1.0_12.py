import codecs
codecs.register_error('strict', codecs.ignore_errors)

#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#from nltk.stem import WordNetLemmatizer
#from nltk.stem.snowball import SnowballStemmer
#from nltk.stem.porter import PorterStemmer
#from nltk.stem.lancaster import LancasterStemmer
#from nltk.stem.isri import ISRIStemmer

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter
