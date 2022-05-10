import select
import socket
import sys
import time
import traceback

from . import __version__
from . import _util
from . import _winapi
from . import constants


__all__ = [
    'Popen',
    'PIPE',
    'STDOUT',
    'DEVNULL',
    'TimeoutExpired',
    'CalledProcessError',
    'SubprocessError',
    'CompletedProcess',
    'run',
    'check_output',
    'call',
    'getoutput',
    'getstatusoutput',
    'getstatus',
]

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
