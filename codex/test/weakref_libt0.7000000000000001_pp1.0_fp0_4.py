import weakref
from collections import namedtuple
from typing import (
    Any,
    Callable,
    Dict,
    Hashable,
    List,
    Optional,
    Set,
    Tuple,
    TYPE_CHECKING,
    Union,
    cast,
)

from typing_extensions import Literal

from . import base, constraints, events, exceptions, notification, plugins
