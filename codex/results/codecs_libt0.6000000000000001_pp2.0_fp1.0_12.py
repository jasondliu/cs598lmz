import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import random
import json
import csv
import math
import re
import shutil

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.python.lib.io import file_io

from bert import modeling
from bert import optimization
from bert import tokenization
from bert import modeling_utils

import pickle

import logging
logging.getLogger().setLevel(logging.INFO)

#--------------------------------------------------------------------------------
# define helper functions
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# load data
#--------------------------------------------------------------------------------

def read_tsv(input_file, quotechar=None):
    """Reads a tab separated value file."""
    with tf.gfile.Open(input_file, "r") as f:
        reader = csv.reader(f, delimiter="\t", quotechar=quotechar)
        lines = []

