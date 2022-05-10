from bz2 import BZ2Decompressor
BZ2Decompressor

# import cPickle
import _pickle as cPickle
cPickle
# import numpy as np
# np

import matplotlib as mpl
mpl

%matplotlib inline
import matplotlib.pyplot as plt
plt

import IPython
IPython
import ipykernel
ipykernel
import IPython.core
IPython.core
import IPython.core.display as _display
_display

import re
re
import os
os

print('confirm non-notebook modules imported')

# import logging
%pylab inline

import nltk
nltk.download('stopwords')

# from nltk.corpus import stopwords
nltk.corpus.stopwords

from nltk.probability import FreqDist
FreqDist

# from string import ascii_lowercase
import string as ascii_lowercase
string as ascii_lowercase

sw = stopwords.words('english')

def rm_stopwords(text):
    return ' '.
