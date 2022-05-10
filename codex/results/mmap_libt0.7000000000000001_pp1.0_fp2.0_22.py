import mmap
import os
import sys
import threading
import time

from ctypes import *

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    import resource
except ImportError:
    resource = None

from . import _os
from . import _threading
from . import _util
from . import _win

from . import _subprocess

from . import _psutil_mswindows
import _psutil_mswindows as cext

# --- constants

CREATE_NEW_CONSOLE = 0x00000010
DETACHED_PROCESS = 0x00000008
PIPE = _subprocess.PIPE
STDOUT = _subprocess.STDOUT
_has_create_job_object = hasattr(cext, "create_job_object")

# --- public functions

def _get_disk_usage(path):
    """Return the disk usage associated with path."""
    drive, _ = os.path.splitdrive(os.path.abspath(path))
    _, _,
