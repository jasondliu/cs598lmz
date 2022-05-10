import gc, weakref
import numpy as np

from contextlib import closing

import logging
logger = logging.getLogger(__name__)

from ctypes import c_size_t

from .util import as_cstr, make_cstr, cstr_array, strArrayType
from . import _libc

# from . import _objgraph

# from . import _memdebug
# _memdebug.set_check_interval(1)


def check_reference_leaks(lib, funcname, n=10):
    """Decorator for checking for reference leaks in a function."""
    def decorator(func):
        def newfunc(*args):
            logger = logging.getLogger(__name__)
            refcounts = {}
            # Get total refcounts
            try:
                state = _objgraph.get_objects()
            except:
                logger.error("Could not examine current refcounts")
            else:
                for x in state:
                    if isinstance(x, lib):
                        refcounts[id(x)] = sys.get
