import gc, weakref
from weakref import WeakValueDictionary
from collections import defaultdict
from copy import copy
from contextlib import contextmanager
from cffi import FFI, CDefError
from ctypes import util, c_void_p
from . import _cffi_backend
from .types import _nonpyobj_fromaddress, _fromaddress

try:
    from _view import ObjectProxy
except ImportError:
    ObjectProxy = None

__all__ = ('PyObjContext', 'PyObj', 'ObjectProxy')

gc_refs = defaultdict(lambda: defaultdict(WeakValueDictionary))

class PyObjContext(object):
    """
    A context manager that executes a block of code in a Python context (ie
    with a reference to a Python object and an appropriate Python exception
    frame) so that Python code and C functions compiled using CFFI ctx.callback
    can be called with CFFI pointers to Python objects.

    The python object is passed as the first argument to the block of code.

    If the argument attribute is True, then the Python object will be
    available as an attribute
