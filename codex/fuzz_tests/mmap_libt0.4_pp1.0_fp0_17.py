import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from enum import Enum
from functools import partial
from itertools import chain

from . import __version__
from . import defaults
from . import util
from . import config
from . import log
from . import path
from . import shell
from . import terminal
from . import vcs
from . import version
from . import xdg

__all__ = ('Project', 'Projects')

logger = log.get_logger(__name__)

# File extensions to ignore when looking for a project file.
IGNORED_EXTENSIONS = (
    '',
    '.pyc',
    '.pyo',
    '.pyd',
    '.so',
    '.o',
    '.a',
    '.exe',
    '.dll',
    '.lib',
    '.obj',
    '.class',
    '.jar',
    '.war',
    '.ear',
    '.zip',
    '.tar',
    '.tgz',
    '.
