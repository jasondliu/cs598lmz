import weakref
import sys
import time

from .core import *
from .debug import *
from .tools import *

from . import core
from . import conf
from . import tools
from . import debug


# -----------------------------------------------------------------------------
#
# LOGGING
#
# -----------------------------------------------------------------------------

def _try_except_log_warning(f, *args, **kwargs):
    try:
        return f(*args, **kwargs)
    except Exception as e:
        log.warning("%s: %s" % (f.__name__, e))


def _try_except_log_warning_and_return_None(f, *args, **kwargs):
    try:
        return f(*args, **kwargs)
    except Exception as e:
        log.warning("%s: %s" % (f.__name__, e))
        return None


# -----------------------------------------------------------------------------
#
# FUNCTIONS
#
# -----------------------------------------------------------------------------


def find_factory_for_file_name(file_name):
    '''
    Find a factory for a given file name.
