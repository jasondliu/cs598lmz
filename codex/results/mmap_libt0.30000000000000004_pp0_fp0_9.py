import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from multiprocessing import Process, Queue, cpu_count
from optparse import OptionParser
from subprocess import Popen, PIPE

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

from pymongo import MongoClient

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

from sklearn.externals import joblib

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_
