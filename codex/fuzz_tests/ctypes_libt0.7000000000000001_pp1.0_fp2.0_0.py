import ctypes
ctypes.c_double_p = ctypes.POINTER(ctypes.c_double)

import os
import sys
from typing import Dict, List

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import OptimizeResult
from scipy.optimize import SR1

from . import _libnlopt
from . import _libnlopt_util
from ._libnlopt_util import NloptError, _Dict2Struct
from .nlopt_constants import algos, local_algos, global_algos
from .nlopt_constants import USER_DEFINED, NLOPT_LN_AUGLAG, NLOPT_LD_AUGLAG
from .nlopt_constants import NLOPT_LN_AUGLAG_EQ, NLOPT_LD_AUGLAG_EQ
from .nlopt_constants import NLOPT_GN_CRS2_LM
from .nlopt_constants import NLOPT_LN_COBYLA, NLOPT_LN
