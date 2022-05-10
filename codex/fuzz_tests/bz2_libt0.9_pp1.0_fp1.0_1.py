import bz2
bz2_text = open('text.bz2', 'r')
print(bz2.decompress(bz2_text.read()).decode('utf-8'))

from functools import partial
from enum import Enum
from blaze import dshape
from datashape import *
from datashape.predicates import *
from collections import namedtuple
from toolz import memoize
from toolz.curried import map, reduce, filter

from operator import add, or_, and_
from datashape import Option, to_numpy_dtype, bool_, any_type
import numpy as np
from numpy import nan
from numpy import datetime64 as dt64
import datetime

from .py2help import _strtypes
from .data import _strategies
from .coretypes import (Fixed, int_dtype, float_dtype, complex_dtype,
                        bool_dtype, object_, string, datetime_,
                        timedelta_, Option, Function, TypeVar)
from blaze.compatibility import reduce

__all__ =
