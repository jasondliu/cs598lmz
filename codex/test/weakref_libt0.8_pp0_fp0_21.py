import weakref
import threading
import collections

from .exceptions import (
    RPCRequestError, RPCResponseError, RPCRemoteError, RPCRemoteWarning)


def rpc(function):
    """
    Wraps an instance method to call that method via RPC.
    """

    def wrapped(self, *args, **kwargs):
        instance = self._get_instance()
        return instance.call_method(function.__name__, args, kwargs)

    return wrapped


def threaded_rpc(function):
    """
    Wraps an instance method to perform an RPC call in a separate thread, and
    update state in the calling thread when results are available (using the
    instance's ``__setattr__`` method).

    This wrapper can be used when a method result is not returned to the caller
    (e.g. if the result is a status code, or if the function returns ``None``).
    """

