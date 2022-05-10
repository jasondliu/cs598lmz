import _struct
import _thread
import _threading
import _timeit
import _token

# Import the built-in version of any modules that have been replaced by our
# own if they are still being imported in user code (this can happen when
# running the test suite).
from collections import OrderedDict
from configparser import ConfigParser
from copy import deepcopy
from functools import reduce
from itertools import zip_longest
from random import random
from sys import intern
from urllib import parse
from types import MappingProxyType

from ._collections_abc import (
    Set, Mapping, Sequence, MutableSet, MutableMapping, MutableSequence,
    ItemsView, KeysView, ValuesView, MappingView
    )

from ._py_compat import unicode, PY2
from ._collections_abc import Hashable

from ._version import __version__, VERSION
from ._compat import (
    StringIO,
    deque,
    )

from .abc import abstractmethod, abstractproperty
from .dataclasses import dataclass, field, fields
