import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

import multiprocessing
import os, sys, re
import argparse
import subprocess
import shlex
import time
import datetime
import random
import numpy as np
import scipy as sp
import scipy.stats
import math
import json
import pandas as pd
import collections
import csv
import io
import itertools
import pickle
import shutil
import glob

# from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence
# from gensim.models.phrases import Phrases, Phraser
# from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# from nltk.tokenize import TweetTokenizer
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.manif
