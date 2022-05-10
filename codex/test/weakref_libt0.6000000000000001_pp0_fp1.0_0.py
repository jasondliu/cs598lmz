import weakref
from weakref import WeakKeyDictionary
from pprint import pformat
from types import MethodType
from collections import defaultdict
from copy import copy, deepcopy

from .utils import (
    is_descriptor,
    is_nonstring_iterable,
    is_parameterized,
    is_dynamic,
    get_parameters,
    get_parameterized_type,
    get_type,
    get_origin,
    get_args,
    get_type_hints,
    get_module_name,
    get_origin_type,
    get_origin_type_name,
    get_args_type_name,
    get_args_type,
    get_type_name,
    get_type_name_or_none,
    get_type_name_or_none,
    get_type_name_or_none,
    get_type_name_or_none,
)

