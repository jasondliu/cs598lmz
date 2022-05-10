import weakref
import re
import os
import sys

from . import _compat
from . import _util
from . import _py2to3
from . import _exceptions
from . import _config
from . import _log
from . import _thread
from . import _process
from . import _util
from . import _compat

_logger = _log.get_logger(__name__)

#------------------------------------------------------------------------------
# Process
#------------------------------------------------------------------------------

class Process(object):
    """
    Represents a process.

    :param int pid:
        Process ID.
    :param str name:
        Process name.
    :param int parent_pid:
        Parent process ID.
    :param str exe:
        Executable path.
    :param str cwd:
        Current working directory.
    :param list cmdline:
        Command line arguments.
    :param dict env:
        Environment variables.
    :param int create_time:
        Process creation time.
    :param int uid:
        User ID.
    :param int gid:
        Group
