from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor()
from cStringIO import StringIO
from tqdm import tqdm
import datetime as dt
import csv
import pandas as pd
import numpy as np
from os.path import walk, dirname, abspath

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from nltk.stem import RSLPStemmer

def to_text():
    base_path = dirname(abspath(__file__))

    movies_list, files_list = [], []

    files = []
    file_list = []

    for (dirpath, dirnames, filenames) in walk(base_path + '/bin/publico-reclamacoes-fundamentadas-sindec-2009-dadosbrutos'):
        files.extend(filenames)
        break

    for filename in tqdm(files):
        file_list.append(dirpath + '\\' + filename
