import gc, weakref
import math
from collections import defaultdict
from typing import (Any, List, Dict, Cast, Hashable, Optional, Tuple, Union,
    overload, Callable, Iterable, Container, AbstractSet)
from abc import ABC, abstractmethod, abstractproperty
from pickle import Pickler, Unpickler
from pickle import HIGHEST_PROTOCOL as PICKLE_PROTOCOL
from pickle import PICKLE_PROTOCOL_VERSION as PICKLE_VERSION
from pickle import PicklingError, UnpicklingError
from typing import TYPE_CHECKING

from ..utils import is_main_thread, nonproxy

if TYPE_CHECKING:
    from .inactive import InactiveList
    from .proxy import Proxy
    from .root import Root, WeakRoot

_id_counter = 0
"""A counter to use for assigning unique ids to objects as they are created."""

_gens = defaultdict(int)
"""A dictionary mapping each object type to the last generation number for
objects of that type."""

_additional_deps = {}
"""A
