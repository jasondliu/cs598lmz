import mmap
import random
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from math import log
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize

# Constants

# Number of top words to print for each category
TOP_COUNT = 20

# Number of words to add to the vocabulary
VOCAB_SIZE = 10000

# Number of documents to read
DOCUMENT_COUNT = 2000

# Number of documents to read in each category
DOCUMENT_COUNT_PER_CATEGORY = 1000

# Number of words to read from each document
WORD_COUNT = 100

# Number of words to read from each document
WORD_COUNT_PER_CATEGORY = 100

# Number of words to read from each document
WORD_COUNT_PER_CATEGORY_TEST = 100

# Number of words to read from each document
WORD_COUNT_
