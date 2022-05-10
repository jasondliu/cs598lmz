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


@table_registry_decorator
def register_type(name: str, length: int=DEFAULT_LENGTH,
                  default: int=DEFAULT_VALUE,
                  structure: Optional[str]=None,
                  decimal: Optional[int]=None):
    """Register a new type to be recognized by ``pandasql``.

    :param name: The name of the type.
    :param length: The length of the type, if applicable. Defaults to the
        default length of the type.
    :param default: The default value for this type. Defaults to ``None``.
    :param structure: The struct format for this type.  Must be present if and
        only
