import mmap
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain, groupby
from operator import attrgetter
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import xattr
from .constants import (
    ATTR_NAME_PREFIX,
    ATTR_NAME_PREFIX_LEN,
    ATTR_NAME_PREFIX_LEN_WITH_SEP,
    ATTR_NAME_PREFIX_WITH_SEP,
    ATTR_NAME_SEP,
    ATTR_NAME_SEP_LEN,
    ATTR_NAME_SEP_LEN_WITH_SEP,
    ATTR_NAME_SEP_WITH_SEP,
    ATTR_NAME_SUFFIX,
    ATTR_NAME_SUFFIX_
