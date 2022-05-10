import gc, weakref, sys
try:
    import lxml
except ImportError:
    pass
import unittest
import os, copy
from operator import itemgetter
from functools import reduce
import operator
from pprint import pprint
from collections import OrderedDict
import numpy as np
import pandas as pd
import scipy.sparse

import Orange
from Orange.data import \
    Table, Domain, ContinuousVariable, DiscreteVariable, StringVariable, \
    Instance, Value
from Orange.data.storage import Storage
from Orange.data.table import \
    Table_from_table, Table_from_domain, Table_from_numpy, Table_from_list
from Orange.data.util import get_unique_names, get_unique_names_duplicates

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class Dummy(object):
    pass


class DummyDiscrete(DiscreteVariable):
    def __init__(self, *args, **kwargs):
        super().__init__(*
