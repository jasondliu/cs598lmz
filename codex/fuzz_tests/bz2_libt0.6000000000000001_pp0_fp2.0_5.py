import bz2
bz2.BZ2File.readline = readline

from os import listdir
from os.path import isfile, join

stop_words = set(stopwords.words('english'))

def get_words(text):
    text = text.lower()
    text = re.sub('<[^<]+>', '', text)
    text = re.sub('[^a-z]+', ' ', text)
    text = text.split()
    text = [w for w in text if w not in stop_words]
    return text

def get_texts(path):
    """
    Reads all text files located in the 'path' and returns a list with all texts concatenated.
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    texts = [open(join(path, f)).read() for f in files]
    texts = ' '.join(texts)
    return texts

def get_texts_list(path):
    """
    Reads all text files located in the '
