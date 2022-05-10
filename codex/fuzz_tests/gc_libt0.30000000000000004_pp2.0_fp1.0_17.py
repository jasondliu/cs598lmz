import gc, weakref
from collections import defaultdict
from collections import deque

from . import _util
from ._util import (
    _is_valid_type,
    _is_valid_type_for_method,
    _is_valid_type_for_property,
    _is_valid_type_for_static_method,
    _is_valid_type_for_static_property,
    _is_valid_type_for_classmethod,
    _is_valid_type_for_classproperty,
    _is_valid_type_for_constructor,
    _is_valid_type_for_function,
    _is_valid_type_for_method_or_property,
    _is_valid_type_for_method_or_static_method,
    _is_valid_type_for_method_or_classmethod,
    _is_valid_type_for_property_or_static_property,
    _is_valid_type_for_property_or_classproperty,
    _is_valid_type_for_method_or_property_or_
