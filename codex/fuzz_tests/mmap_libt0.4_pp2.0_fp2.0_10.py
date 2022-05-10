import mmap
import os
import re
import sys
import time
import traceback

from . import util
from . import __version__
from . import __author__
from . import __license__
from . import __doc__
from . import __url__
from . import __copyright__

# ------------------------------------------------------------------------------
#
class Syslog(object):
    """
    Syslog class.

    This class provides an interface to the syslog(3) system log module.

    Typical usage:

    >>> import syslog
    >>> syslog.openlog('myapp', syslog.LOG_PID)
    >>> syslog.syslog(syslog.LOG_INFO, 'Program started')
    >>> syslog.syslog(syslog.LOG_INFO, 'A number: %d' % 42)
    >>> syslog.closelog()

    """

    # --------------------------------------------------------------------------
    #
    def __init__(self):

        self._ident = None
        self._logopt = None
        self._facility = None

        self._log_mask = 0
        self._log_facility =
