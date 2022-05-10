import codecs
codecs.register_error('strict', codecs.ignore_errors)

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object, map, zip)
from future.utils import iteritems

from scipy.sparse import csr_matrix, vstack
from sklearn.base import TransformerMixin
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

from feature_extraction import extract_features
from feature_extraction import get_dataset
from feature_extraction import get_dataset_from_annotated
from feature_extraction import get_dataset_from_gold

