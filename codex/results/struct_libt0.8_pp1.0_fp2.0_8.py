import _struct
from array import array
from math import hypot, isfinite
import bz2
from collections import OrderedDict
from collections.abc import Mapping
from numbers import Integral
from pathlib import Path
from warnings import warn
import weakref
from xml.etree import ElementTree
from typing import (
    List,
    Tuple,
    Optional,
    Union,
    IO,
    Any,
    Callable,
    Iterable,
    Iterator,
    Sequence,
    Mapping as MappingType,
    Dict,
    Type,
    Union as UnionType,
    Optional as OptionalType,
    TypeVar,
    ClassVar,
    cast,
)
import numpy as np
from nptyping import NDArray, Array
import typing_inspect
from typing_extensions import Literal

from ._utils import (
    _read_sizes,
    _get_array_count,
    _to_str,
    ByteOrder,
    _tiff_to_numpy_dtype,
    _read_tiff_header,

