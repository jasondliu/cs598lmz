import mmap
import os
import re
import sys
import time

from functools import partial
from multiprocessing import Pool
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import version_utils
from .constants import (
    DEFAULT_CONFIG_DIR,
    DEFAULT_CONFIG_FILE,
    DEFAULT_DATA_DIR,
    DEFAULT_LOG_DIR,
    DEFAULT_LOG_FILE,
    DEFAULT_PID_DIR,
    DEFAULT_PID_FILE,
    DEFAULT_RUN_DIR,
    DEFAULT_RUN_FILE,
    DEFAULT_SOCKET_DIR,
    DEFAULT_SOCKET_FILE,
    DEFAULT_WORK_DIR,
    DEFAULT_WORK_FILE,
    DEFAULT_WORK_TEMP_DIR,
    DEFAULT_WORK_TEMP_FILE,
    DEFAULT_WORK_TEMP_PREFIX,

