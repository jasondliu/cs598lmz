import mmap
import os
import sys

from collections import defaultdict
from itertools import islice
from typing import Dict, List, Tuple

import numpy as np

from .base_index import BaseIndex
from .constants import (
    KEY_BYTES,
    VALUE_BYTES,
    MAX_KEY_VALUE_PAIRS,
    MAX_KEY_VALUE_PAIRS_BYTES,
    MAX_KEY_VALUE_PAIRS_BYTES_BYTES,
    MAX_KEY_VALUE_PAIRS_BYTES_SIZE,
    MAX_KEY_VALUE_PAIRS_SIZE,
    MAX_KEY_VALUE_PAIRS_SIZE_BYTES,
    MAX_KEY_VALUE_PAIRS_SIZE_SIZE,
    MAX_KEY_VALUE_PAIRS_SIZE_SIZE_BYTES,
    MAX_KEY_VALUE_PAIRS_SIZE_SIZE_SIZE,
    MAX_KEY_VALUE_PAIRS_SIZE_SIZE_SIZE_BYTES,
    MAX_KEY_VALUE
