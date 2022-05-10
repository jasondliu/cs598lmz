import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)
import h5py
import pandas as pd
import seaborn as sns
import numpy as np
import scipy as sp
from subprocess import Popen, PIPE
import os
import sys
import re
import json
import time
import subprocess
import threading
from collections import Counter, defaultdict
from itertools import product
import string
import multiprocessing
from multiprocessing import Process, Queue
from scipy.stats import pearsonr, spearmanr
from scipy.spatial.distance import cosine, cityblock, jaccard, canberra, euclidean, minkowski, braycurtis
from nltk.util import ngrams
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import normalize
from sklearn.decomposition
