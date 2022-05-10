import codecs
codecs.register_error('strict', codecs.ignore_errors)
from lxml import etree, html
from pprint import pprint
import re
from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner
from lxml.html.soupparser import fromstring, tostring
from HTMLParser import HTMLParser
from lxml.cssselect import CSSSelector
import cssselect

import os
import sys
from collections import OrderedDict
from datetime import datetime

#from lxml.html.clean import Cleaner
#from lxml.html.soupparser import fromstring, tostring

from unidecode import unidecode

from itertools import izip
from itertools import chain

from difflib import SequenceMatcher

from operator import itemgetter

from re import compile
from datetime import datetime

from math import log, sqrt

from numpy import *
from numpy import *
from numpy import dot
from scipy.linalg import norm

from sklearn.feature_extraction.text import Tfidf
