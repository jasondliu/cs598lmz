import weakref

from . import _base
from . import _compat
from . import _util

__all__ = [
    'Pool',
    'PoolConnection',
    'PoolConnectionContext',
    'PoolConnectionProxy',
    'PoolContext',
    'PoolError',
    'PoolFull',
    'PoolListener',
    'PoolListenerContext',
    'PoolListenerProxy',
    'PoolProxy',
    'PoolTimeout',
    'PoolTransaction',
    'PoolTransactionContext',
    'PoolTransactionProxy',
]


class PoolError(_base.Error):
    """Base class for all pool errors."""


class PoolFull(PoolError):
    """The pool is full."""


class PoolTimeout(PoolError):
    """The pool timed out."""


class PoolListener(object):
    """A listener for pool events.

    :param pool: The pool to listen to.
    :type pool: :class:`Pool`

    """

    def __init__(self, pool):
        self._pool = weakref.ref(pool)

    @property
   
