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

__all__ = [
    'SBM', 'SBM_degree_corrected', 'SBM_degree_corrected_entropy',
    'SBM_degree_corrected_entropy_parallel', 'SBM_degree_corrected_entropy_parallel_profile',
    'SBM_degree_corrected_entropy_parallel_profile_predict', 'SBM_degree_corrected_entropy_parallel_profile_predict_step',
    'SBM_degree_corrected
