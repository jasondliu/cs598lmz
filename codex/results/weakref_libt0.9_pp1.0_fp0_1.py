import weakref
import os.path
from ctypes import OID, mx_from_int
from copy import copy, deepcopy
import collections
from operator import methodcaller
from . import terminators
from . import heuristics
from . import gc
from . import exc

from logging import getLogger
logger = getLogger(__name__)

def detect_type(item):
    # type: (Any) -> str
    if isinstance(item, MxObject):
        return 'mx-object'
    elif isinstance(item, mx_from_int):
        return 'oid'
    elif isinstance(item, (list, tuple, Iterable)):
        return 'iterable'
    elif isinstance(item, (bool, str, int)):
        return 'basic'
    else:
        raise RuntimeError(
            'Value is of unknown type and cannot be saved in an mxgraph: %r (%r)'
            % (item, item.__class__))

class Tag(object):
    def __init__(self, handle=None,
