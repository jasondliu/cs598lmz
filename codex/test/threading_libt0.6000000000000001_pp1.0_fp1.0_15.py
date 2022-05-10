import threading
threading.stack_size(2**27)
import sys
import re
import math
import os
import numpy as np
from time import time
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import scipy.sparse as sp
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from scipy.sparse.linalg import svds
from numpy.linalg import norm
from numpy import dot
import numpy as np
import pandas as pd
import requests
import ast
import json
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
import re
import nltk
from nltk.stem.porter import PorterStemmer
import pickle

nltk.download('wordnet')
nltk.download('stopwords')

import warnings
warnings.filterwarnings('ignore')

from nltk.corpus import stopwords
