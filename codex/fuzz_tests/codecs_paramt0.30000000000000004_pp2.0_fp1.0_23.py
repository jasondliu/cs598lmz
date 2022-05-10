import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import json
import time
import logging
import argparse
import traceback
import subprocess
from collections import defaultdict
from itertools import chain
from multiprocessing import Pool, cpu_count
from functools import partial
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bs4.element import Comment
from bs4.element import NavigableString
from bs4.element import Tag

from lxml import etree
from lxml.etree import XMLSyntaxError
from lxml.html import HTMLParser
from lxml.html import fromstring
from lxml.html import tostring

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import Count
