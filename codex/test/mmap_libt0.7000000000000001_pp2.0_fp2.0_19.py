import mmap
import os
import sys
import time

import numpy as np
from scipy.sparse import csr_matrix

from future.utils import viewitems

from .vocab import Vocab
from .utils import pickle_load, pickle_dump, get_model_name


class Embeddings:
    """
    Class for loading and using embeddings.

    :param vocab: Vocab object
    :param wv_type: one of {'', '', ''}
    :param kwargs: used to pass parameters to the actual word2vec implementation
    """

    def __init__(self, vocab, wv_type='', **kwargs):
        self.wv_type = wv_type.lower()
