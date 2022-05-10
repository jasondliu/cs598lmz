import selectors
import time
import sys
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import math
import operator

#-----------------------------------------------------------------------------------
#----------------------------Global Variables---------------------------------------
#-----------------------------------------------------------------------------------

#Dictionary to store all the links
all_links = {}

#Dictionary to store all the links
all_links_for_index = {}

#Dictionary to store all the links
all_links_for_index_with_title = {}

#Dictionary to store all the links
