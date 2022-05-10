import gc, weakref
from itertools import count
from collections import defaultdict

from .. import util
from ..util import Cached
from . import core
from .core import (
    Subscription,
    SubscriptionMixin,
    )

class AsyncResult(SubscriptionMixin):
    """A result of an asynchronous operation.

    This class is a convenient wrapper around
    :class:`asyncio.Future` class.
    
    :class:`AsyncResult` objects can be used as a context manager::

        >>> result = AsyncResult()
        >>> with result:
        ...     pass

    :class:`AsyncResult` objects can be used as a context manager::

        >>> result = AsyncResult()
        >>> with result:
        ...     pass

    """
    __slots__ = ('_future', '_callbacks', '_done_callbacks')

    def __init__(self):
        super(AsyncResult, self).__init__()
        self._future = asyncio.Future()
        self._callbacks = []
        self._done_callbacks = []

    def
