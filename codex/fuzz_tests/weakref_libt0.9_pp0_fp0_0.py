import weakref
import multiprocessing as mp
from time import time
import logging

import numpy as np
import pandas as pd

from . import npfloat64
from . import npfloat32
from . import npint
from . import npint64
from . import npint32
from . import _common as common


class Table(object):
    """Implementation of the Table class.

    It provides a simple interface to the underlying data in memory.

    Parameters:
    -----------
    header: str
            Path to header file in mrc file format.
    data: int, optional
          Path to data file in mrc file format. If not provided, the path to
          the data file will be set to the same as the header file.
    labels: int, optional
            Path to data file in mrc file format. If not provided, the path to
            the data file will be set to the same as the header file.
    **kwargs: Keyword arguments
              Additional keyword arguments. Forwarded to the pandas.read_csv function.

    Attributes:
    -----------
    dtype: numpy
