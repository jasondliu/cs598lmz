import weakref

from . import get_debug_flag
from . import logger, log_level

if get_debug_flag():
    # this is a trick to make the "assert" statement
    # to be compiled even in release mode.
    def __assert(cond):
        if not cond:
            raise Exception("Assertion Failed")
