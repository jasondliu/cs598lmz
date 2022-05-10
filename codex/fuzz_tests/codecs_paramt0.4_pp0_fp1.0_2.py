import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys

import numpy as np
import tensorflow as tf

from tensorflow.python.ops import lookup_ops

from data_utils import load_vocab
from data_utils import load_embedding_vectors_glove
from data_utils import create_vocabulary
from data_utils import sentence_to_token_ids


def read_data(source_path, target_path, max_size=None):
    """Read data from source and target files and put into buckets.

    Args:
      source_path: path to the files with token-ids for the source language.
      target_path: path to the file with token-ids for the target language;
        it must be aligned with the source file: n-th line contains the desired
        output for n-th line from the source_path.
      max_size: maximum number of lines to read, all other will be ignored;
        if 0 or None, data files will be read completely (no limit).

    Returns:
      data_set: a list of
