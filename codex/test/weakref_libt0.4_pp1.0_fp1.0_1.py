import weakref

from . import _internal
from . import _util
from . import _types
from . import _errors
from . import _base


def _make_weak_method(method):
    """
    Make a weak reference to a bound method.

    :param method:
        The method to make weak.

    :returns:
        A weak reference to the method.
    """
    if sys.version_info[0] >= 3:
        return weakref.WeakMethod(method)
    else:
        return weakref.proxy(method)


class _Callback(object):
    """
    Callback for a specific event.
    """

