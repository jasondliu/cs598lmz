import mmap
import os
import shlex
import subprocess
import time
from datetime import timedelta
from distutils.version import LooseVersion
from functools import lru_cache
from itertools import chain
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Tuple,
    Type,
    Union,
)
from warnings import warn

from . import __version__


@lru_cache()
def _get_pandas_version() -> str:
    """Return the current version of pandas."""
    import pandas as pd

    return LooseVersion(pd.__version__).vstring


def _get_pandas_ver_tuple(version: str = None) -> Tuple[int, ...]:
    """Return the current version of pandas as a tuple of ints.

    Converts to ints for backwards compatibility
    """
