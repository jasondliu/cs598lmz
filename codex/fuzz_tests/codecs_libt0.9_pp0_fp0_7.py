import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import math
import csv
from enum import Enum
from os.path import join
import re
import itertools

sys.path.append(os.path.join(os.getcwd(), ".."))
from utilities import ml_utilities, ml_utilities as utils
from utilities import ml_math
from utilities import ml_file


class OutlierDetection(Enum):
    MedianAbsoluteDeviation = 1
    AverageAbsoluteDeviation = 2
    ZScore = 3


class OutlierResult:
    """ Container class used by IsOutlier method to report outliers. """

    def __init__(self, outliers: list, total: int):
        """OutlierResult Constructor.

        Args:
          outliers: List of outlier values.
          total: Total number of values.

        """
        self.outliers = outliers
        self.total = total

    def __str__(self):
