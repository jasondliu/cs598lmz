import mmap
import os
import time
import pickle
from typing import List
from typing import Tuple
from typing import Dict
from typing import Set
from typing import Optional
from typing import Union
from typing import Any
from typing import NamedTuple
from typing import Iterable
from typing import Callable
from typing import cast
from typing import TYPE_CHECKING

from . import util


if TYPE_CHECKING:
    from .typing import TypeValue  # noqa: F401


def _dict_difference(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    return dict(a, **b)


def _get_size(obj: object, seen: Set[int]) -> int:
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if id(obj) in seen:
        return size
    seen.add(id(obj))
    if isinstance(obj, dict):
        size += sum([_get_size(v, seen) for v in obj.values()])
