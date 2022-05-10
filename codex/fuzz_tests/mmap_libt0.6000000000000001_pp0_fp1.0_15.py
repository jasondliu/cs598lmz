import mmap
import os
import re
import sys
from typing import Any, Dict, List, Optional, Union

from . import utils
from .exceptions import (
    ConfigSyntaxError,
    ConfigTypeError,
    ConfigValueError,
    NoSectionError,
    NoOptionError,
    ParsingError,
    MissingSectionHeaderError,
)
from .utils import _ChainMap, _ChainMapDict, _ChainMapList
from .utils import _ChainMapListDict, _ChainMapListDictStr
from .utils import _ChainMapDictStr, _ChainMapListStr, _ChainMapStr
from .utils import _ChainMapStrDict, _ChainMapStrList, _ChainMapStrListDict
from .utils import _ChainMapStrListDictStr, _ChainMapStrDictStr, _ChainMapStrStr
from .utils import _ChainMapTuple, _ChainMapTupleDict, _ChainMapTupleList
from .utils import _ChainMapTupleListDict, _ChainMapTupleListDictStr
from .utils import _ChainMapTupleDict
