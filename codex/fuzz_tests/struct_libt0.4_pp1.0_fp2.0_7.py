import _struct
import sys
import time
import threading
import traceback
import types
import warnings

from . import _compat
from . import _util
from . import _winreg
from . import _winapi

from . import _winapi
from . import _winreg
from . import _util
from . import _compat

__all__ = ['Popen', 'PIPE', 'STDOUT', 'call', 'check_call', 'getstatusoutput',
           'getoutput', 'check_output', 'CalledProcessError', 'TimeoutExpired']

# Exception classes used by this module.
class CalledProcessError(Exception):
    """This exception is raised when a process run by check_call() or
    check_output() returns a non-zero exit status.
    The exit status will be stored in the returncode attribute;
    check_output() will also store the output in the output attribute.
    """
    def __init__(self, returncode, cmd, output=None):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
    def
