import weakref
from collections import defaultdict
from functools import wraps

from . import _logging as logging
from . import log_context
from . import errors
from . import util


__all__ = (
    "QualifiedFunction",
    "MethodProxy",
    "QualifiedName",
    "OverloadedFunction",
    "overload",
)


class QualifiedFunction(object):
    def __init__(self, func, qualified_name):
        self._func = func
        self._qualified_name = qualified_name

    def __repr__(self):
        return "<QualifiedFunction: %s>" % self.qualified_name

    @property
    def qualified_name(self):
        return self._qualified_name

    @property
    def func(self):
        return self._func

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)


class MethodProxy(object):
    def __init__(self, obj, func, qualified_name):
        self._obj = obj
        self._func
