import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from keras.models import load_model
import unicodedata
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

def strip_accents(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii','ignore')
    text = text.decode("utf-8")
    return text

def remove_punctuation(text):
    return ''.join(w for w in text if w not in punctuation)

def remove_stopwords(text):
    return ' '.join(w for w in text.split() if w not in stopwords.words('spanish'))

def stem_text(text):
    porter = PorterStemmer()
    return ' '.join([porter.stem(text)])

def lemmatize_text(text):
    wordnet
