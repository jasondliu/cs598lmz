import ctypes
ctypes.cast(0, ctypes.py_object)

import os
from typing import Dict, List
from pathlib import Path
import re
from collections import defaultdict
from math import ceil, floor

from pandas import DataFrame
import numpy as np
from nltk.tokenize import sent_tokenize

from faro_common.faro_common import *
from faro_common.product import *
from faro_common.image import *


def csv_to_df(csv_path: Path, **kwargs) -> DataFrame:
    return DataFrame.from_dict(csv_to_dict(csv_path), **kwargs)


def csv_to_dict(csv_path: Path, **kwargs) -> Dict:
    return tsv_to_dict(csv_path, sep=',', **kwargs)


def tsv_to_dict(tsv_path: Path, **kwargs) -> Dict:
    with open(tsv_path) as f:
        first_line = f.readline()
        if not first_line
