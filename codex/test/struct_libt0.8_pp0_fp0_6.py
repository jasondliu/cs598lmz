import _struct
from collections import namedtuple
from typing import List, Optional
from uuid import uuid4

from ._compat import TEXT_TYPE, TYPES
from ._errors import TableRegistryError
from ._util import table, table_registry_decorator

DEFAULT_VALUE = object()
DEFAULT_LENGTH = object()

_Type = namedtuple('Type', 'name length default')


