import weakref
#from numpy.lib import function_base as _function_base
from .. import _function_base
import multiprocessing
import itertools
import operator
from .. import utils
from ..utils import isinstance_
from ..utils import Progress
import re
import os
import warnings
from ..utils import format_dict


RE_CAMEL = re.compile(r'([A-Z][a-z]*)(\d+|[A-Z][a-z]*|$)')


# Handy functions

def get_namespace(ns):
    """Return namespace corresponding to ns

    Examples
    --------
    >>> get_namespace('traits')['Scalar'] # doctest: +ELLIPSIS
    <class 'traits.traits.Scalar'>

    >>> get_namespace('numpy')['array'] # doctest: +ELLIPSIS
    <built-in function array>

    TODO: refactor in pyopendata
    """
    import sys
    d = sys.modules[ns]
    out = {}
   
