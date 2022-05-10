import weakref
from contextlib import contextmanager
from functools import partial
from itertools import chain
from operator import attrgetter
from pathlib import Path
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
    cast,
)
