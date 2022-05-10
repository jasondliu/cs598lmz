import mmap
import os
import re
import sys
import time
import traceback
from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow.parquet import ParquetFile
from tqdm import tqdm

from . import __version__
from .config import Config
from .constants import (
    DEFAULT_COLUMN_TYPES,
    DEFAULT_DATE_COLUMNS,
    DEFAULT_DATETIME_COLUMNS,
    DEFAULT_DATETIME_FORMAT,
    DEFAULT_DATETIME_UNITS,
    DEFAULT_DELIMITER,
    DEFAULT_FLOAT_COLUMNS,
    DEFAULT
