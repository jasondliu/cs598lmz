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

    def __init__(self, callback, on_error, on_remove,
                 remove_on_error, remove_on_completion):
        """
        :param callback:
            The callback to invoke.

        :param on_error:
            The error handler callback.

        :param on_remove:
            The callback to invoke when the callback is removed.

        :param remove_on_error:
            Whether the callback should be removed when
