import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from . import config
from . import constants
from . import util
from . import version

# TODO: Remove this when we drop Python 2.6 support.
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

# TODO: Remove this when we drop Python 2.6 support.
try:
    from collections import Counter
except ImportError:
    from counter import Counter

# TODO: Remove this when we drop Python 2.6 support.
try:
    from collections import namedtuple
except ImportError:
    from namedtuple import namedtuple

# TODO: Remove this when we drop Python 2.6 support.
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

try:
    from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Tuple, Union 
