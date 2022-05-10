import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from urllib.parse import urlparse
import urllib
from flask import Flask, render_template, request
from DB.mysql import *
from DB.mysql_conn import *

from flask_cache import Cache
import re
from pyltp import Segmentor
from pyltp import SentenceSplitter
import jieba
from jieba import posseg
import jieba.analyse
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.datasets.base import Bunch
import pandas as pd
from sklearn.externals import joblib
from sklearn.model_
