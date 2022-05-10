import _struct
from collections import namedtuple
from math import ceil, log
from random import randint

import numpy as np
from scipy.optimize import minimize
from scipy.special import gamma, gammaln

from . import base
from . import exceptions
from . import utils

# Late import of python-igraph to avoid dependency
try:
    import igraph
except ImportError:
    igraph = None

# Late import of networkx to avoid dependency
try:
    import networkx as nx
except ImportError:
    nx = None

