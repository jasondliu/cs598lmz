import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

from collections import defaultdict
from itertools import islice
import os
import random
import re
import sys
import time
import traceback

import numpy
import pymongo
import scipy.sparse
import sklearn.feature_extraction.text
import sklearn.linear_model
import sklearn.metrics
import sklearn.pipeline
import sklearn.preprocessing
import sklearn.svm

import nlp
import nlp.tokenize
import nlp.vectorize
import nlp.classify
import nlp.classify.text
import nlp.classify.text.svm
import nlp.classify.text.svm.predict
import nlp.classify.text.svm.train
import nlp.classify.text.svm.train_models
import nlp.classify.text.svm.train_models_with_crossvalidation
import nlp.classify.text.svm.train_models
