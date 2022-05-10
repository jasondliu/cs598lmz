import gc, weakref
import inspect, logging
try:
    # New in Python 2.5
    import __builtin__
    exit_func = __builtin__.exit
    del __builtin__
except ImportError:
    import sys
    exit_func = sys.exit
    del sys

from sitedjango.models import *
from sitedjango.user import *


def recursive_eq(left, right):
    """returns True iff left and right have the same value

    this assumes that __eq__ and __hash__ are sane. This is more of
    a shim of some Python users who have a tendency to define silly
    equality methods"""
    try:
        return left == right
    except Exception:
        return False
    finally:
        del left, right

def recursive_repr(value, maxdepth=12, maxlist=20, maxstring=200):
    """computes a mostly-complete, mostly-safe repr of nested objects

    designed as an alternative to builtin repr, which can be unsafe
    (infinite recursion) and incomplete (list contents shown as
   
