from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

if sys.version_info[0] >= 3:
    from io import BytesIO
    from urllib.request import urlopen
else:
    from StringIO import StringIO as BytesIO
    from urllib2 import urlopen

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

from utils import load_data, load_glove_embeddings, load_stanford_glove_embeddings, load_stanford_glove_embeddings_lower
from utils import load_google_word2vec_embeddings, load_google_word2vec_embeddings_lower
from utils import load_word2vec_embeddings, load_word2vec_embeddings_lower
from utils import load_gensim_word2vec_embeddings, load_gensim_word2vec_embed
