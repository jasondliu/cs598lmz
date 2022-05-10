import lzma
lzma.LZMADecompressor.decompress(open("github_data.xz", "rb").read()).decode("utf-8")

from gensim.models import word2vec
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.models.word2vec import LineSentence

from tqdm import tqdm
from tqdm import tqdm_notebook

tqdm.pandas(tqdm_notebook)

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from collections import OrderedDict

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from nltk.corpus import stopwords
from nltk.cluster import KMeansClusterer
from nltk import FreqDist
from nltk import word_tokenize
from nltk
