import _struct
from binascii import hexlify
from collections import namedtuple
from functools import partial
from itertools import chain, repeat
from operator import itemgetter
from struct import Struct
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

from . import _compat
from . import _constants
from . import _errors
from . import _types
from . import _utils

#: The default buffer size for :class:`~.BufferedReader`.
DEFAULT_BUFFER_SIZE = 1024 * 1024

#: The default buffer size for :class:`~.BufferedWriter`.
DEFAULT_BUFFER_SIZE = 1024 * 1024

#: The default buffer size for :class:`~.BufferedRandom`.
DEFAULT_BUFFER_SIZE = 1024 * 1024

#: The default buffer size for :class:`~.BufferedRWPair`.
DEFAULT_BUFFER_SIZE = 1024 * 1024

#: The default buffer size for :class:`~.BufferedDuplex`.
DEFAULT_BUFFER_
