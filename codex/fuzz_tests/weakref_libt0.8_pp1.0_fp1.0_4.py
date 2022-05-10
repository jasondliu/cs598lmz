import weakref
from collections import namedtuple

from .. import exceptions

__all__ = [
    "null",
    "get",
    "scope",
    "singleton",
    "bind",
    "factory",
    "inject",
]

SCOPE_UNIQUE = object()
SCOPE_SINGLETON = "singleton"
SCOPE_REQUEST = "request"
SCOPE_THREAD = "thread"
SCOPE_NO_OVERRIDE = object()

_Scope = namedtuple("_Scope", ("value", "parent"))
_Binding = namedtuple("_Binding", ("instance", "scope"))
_Mark = namedtuple("_Mark", ("value", "message"))
_DeepMark = namedtuple("_DeepMark", ("value", "message", "depth"))
_Factory = namedtuple("_Factory", ("func", "scope"))
_RuntimeException = namedtuple("_RuntimeException", ("message",))


class ScopeStack:
    def __init__(self):
        self._scopes = []

    def push(self
