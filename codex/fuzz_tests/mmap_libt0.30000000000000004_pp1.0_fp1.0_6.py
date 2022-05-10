import mmap
import os
import sys
import time

from collections import defaultdict
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from os import path
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import requests
import tqdm
from fastparquet import ParquetFile
from pandas.api.types import is_categorical_dtype
from pandas.core.dtypes.common import is_datetime64_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.indexes.period import PeriodIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.core.indexes.tim
