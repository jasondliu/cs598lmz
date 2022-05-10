import codecs
codecs.register_error('replace_space',replace_space)
# encoding=utf-8
import sys
import os
import spacy
import numpy as np
import codecs
from nltk import Tree
import re
from nltk.stem import WordNetLemmatizer
import json
from json.decoder import JSONDecodeError
from spacy.pipeline import EntityRuler
from tqdm import tqdm
from spacy.gold import GoldParse
from spacy.scorer import Scorer
from spacy.util import minibatch, compounding
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
from sklearn.externals import joblib
import time
import math

class CRFExtractor(object):
    """A class for extracting entity mentions
