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

