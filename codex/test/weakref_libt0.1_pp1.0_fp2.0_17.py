import weakref

from . import _base
from . import _compat
from . import _util
from . import _vendor
from . import _vendor_packages
from . import exceptions
from . import interfaces
from . import util

_logger = _util.get_logger(__name__)

_registry = weakref.WeakValueDictionary()


def _get_registry():
    return _registry


def _get_registry_key(cls, name):
    return (cls, name)


def _get_registry_value(cls, name):
    return _get_registry().get(_get_registry_key(cls, name))


def _set_registry_value(cls, name, value):
    _get_registry()[_get_registry_key(cls, name)] = value


def _del_registry_value(cls, name):
    del _get_registry()[_get_registry_key(cls, name)]

