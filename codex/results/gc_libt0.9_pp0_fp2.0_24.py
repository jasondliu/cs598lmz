import gc, weakref
from numbers import Number
from functools import reduce, partial
from operator import mul

from sys import intern
from types import BuiltinFunctionType, MethodType, BuiltinMethodType, FunctionType
from itertools import product
from weakref import ReferenceType
from collections import Set, Mapping, Sequence, Iterable
from textwrap import dedent

from .pixeldata import PixelData
from .units import seconds, ms, Hz, kHz

from .constants import type_registry, default_type_registry, type_list
from .util import cached_class_property, compute_tag_id
from warnings import warn
from copy import copy
from functools import lru_cache
from itertools import groupby

from .protocols import _dtype_to_scalar_type
from .protocols import _array_to_pixeldata, _pixeldata_to_shape, _value_to_array
from .protocols import _array_to_value, _shape_to_size, _array_to_dtype
from .protocol
