import weakref
from datetime import datetime
from enum import Enum
from logging import getLogger
from pathlib import Path
from typing import List, Tuple, Optional, Union, Sequence, Dict, Type, Callable

from . import _base, _enum, _util
from .exception import *
from .field import *
from .version import *

# List of formats supported by the library.
_FORMATS = [
    'odf',
    'odt',
    'ods',
    'odp',
    'odg',
    'fodt',
    'fods',
    'fodp',
    'fodg',
    'ott',
    'ots',
    'otp',
    'otg',
    'odc',
    'odi',
    'otc',
    'oti',
    'oth',
    'odf',
]
