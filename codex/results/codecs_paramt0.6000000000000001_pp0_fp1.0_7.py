import codecs
codecs.register_error("strict", codecs.ignore_errors)

import os
import sys
import inspect
import types
import re
import time
import gc
import itertools
import subprocess
import traceback
import pprint
import functools
import collections
from contextlib import contextmanager

import numpy
import numpy as np
import scipy
import scipy.optimize
import scipy.signal
import scipy.ndimage
import scipy.integrate
import scipy.stats
import scipy.sparse
import scipy.sparse.linalg
import scipy.special
import scipy.interpolate
import scipy.misc

from numpy import frompyfunc, float32, float64, float128, int32, int64, complex64, complex128, complex256, nan, inf, pi, e, exp, log, log10, sqrt, cos, sin, tan, arcsin, arccos, arctan, arctan2, sinh, cosh, tanh, arcsinh, arccosh, ar
