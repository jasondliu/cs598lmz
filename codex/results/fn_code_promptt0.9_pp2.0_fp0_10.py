fn = lambda: None
# Test fn.__code__ is not None
setattr(fn, '__code__', None)

from functools import partial
from types import MethodType
from typing import Any, Callable, no_type_check

from xotl.fl import PARAM, actual

from ._meta import abc_extension_type
from .layout import Layout, Layoutable
from .scope import Scope, SortedScope, is_shared
from .signature import Signature
from .util import (
    is_private,
    resolve_dotted_name,
    resolve_textual_name,
    Undefined,
    dispatching_error,
)


class MethodMeta(abc_extension_type):
    __slots__ = ('method_id', 'signature')

    def __init__(self, method_id, signature):
        self.method_id = method_id
        self.signature = signature

    def _as_function(self, method):
        assert isinstance(method, BoundMethod)
        assert method.identity == self.method_id
        m = method._fn
        assert isinstance
