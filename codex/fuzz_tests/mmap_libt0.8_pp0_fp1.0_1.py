import mmap
import os
from collections import Counter
from scipy.sparse import coo_matrix, isspmatrix, csr_matrix
import numpy as np
from sklearn.utils import murmurhash3_32
from sklearn.utils import check_random_state
from sklearn.exceptions import NotFittedError
from sklearn.externals import six
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import HashingVectorizer
from tabulate import tabulate
import re
from itertools import chain
import logging

from datasketch import MinHash, MinHashLSHForest

logger = logging.getLogger(__name__)

class EntityExtractor:
    """
    Transformer which will extract entities from a list of text documents
    """
    def __init__(self, ngram_range=(1,3), hash_size=200000,
                 token_extraction_strategy='hashing'):
        """
        Arguments:
        ngram_range -- tuple of the minimum size and maximum
