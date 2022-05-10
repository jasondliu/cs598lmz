import _struct
import logging
import os
import struct
import time
from collections import defaultdict
from functools import reduce

import numpy as np
import pandas as pd

from . import util
from .util import get_logger
from .util import get_store, get_store_path
from .util import hash_dict, hash_list, hash_str
from .util import to_hash_str
from .util import zip_str, unzip_str

# ------------------------------------------------------------------------------
#
# Constants.
#
# ------------------------------------------------------------------------------

logger = get_logger(__name__)

# ------------------------------------------------------------------------------
#
# Dataset.
#
# ------------------------------------------------------------------------------

def _hash_file(file_path):
    with open(file_path, 'rb') as file:
        hash_ = hashlib.sha1()
        while True:
            data = file.read(65536)
            if not data:
                break
            hash_.update(data)
        return hash_.hexdigest()


class Dataset(object):

    def __init__(self
