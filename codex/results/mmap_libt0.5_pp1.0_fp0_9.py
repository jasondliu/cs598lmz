import mmap
import os
import re
import struct
import subprocess
import sys
import tempfile
import time

import psutil

from . import __version__
from . import util
from . import _constants
from . import _util

_log = logging.getLogger(__name__)

# Exported symbols.
__all__ = [
    # Constants.
    'PROT_READ', 'PROT_WRITE', 'PROT_EXEC', 'PROT_NONE',
    'MAP_SHARED', 'MAP_PRIVATE', 'MAP_ANONYMOUS', 'MAP_ANON',
    'MAP_GROWSDOWN', 'MAP_DENYWRITE', 'MAP_EXECUTABLE', 'MAP_LOCKED',
    'MAP_NORESERVE', 'MAP_POPULATE', 'MAP_NONBLOCK', 'MAP_STACK',
    'MAP_HUGETLB', 'MAP_32BIT', 'MAP_RANDOM', 'MAP_FIXED',

    # Functions.
    'process_iter', 'process_
