import mmap
import os
import sys
import time

from collections import defaultdict
from itertools import chain
from operator import itemgetter
from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Set, Tuple

from . import __version__
from . import config
from . import constants
from . import errors
from . import file_utils
from . import git_utils
from . import log
from . import utils
from . import vcs_utils
from . import version_utils
from . import virtualenv
from . import virtualenv_utils
from . import wheel_utils
from .config import Config
from .constants import (
    DEFAULT_INDEX_URL,
    DEFAULT_PIP_VERSION,
    DEFAULT_PYTHON_VERSION,
    DEFAULT_REQUIREMENTS_FILE,
    DEFAULT_SOURCE,
    DEFAULT_TIMEOUT,
    DEFAULT_VERBOSITY,
    DEFAULT_VIRTUALENV_BACKEND,
    DEFAULT_VIRTUALENV_PYTHON,
    DEFAULT_V
