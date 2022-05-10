import weakref as _weakref
from future.utils import PY2

from gevent.event import AbstractEvent
from gevent.event import _thread


def _cancelled(orig_error):
    return isinstance(orig_error, _BaseException)


if PY2:
    _BaseException = BaseException
else:
    _BaseException = Exception

__all__ = ['AsyncResult']


class AsyncResult(AbstractEvent):

    def __init__(self):
        AbstractEvent.__init__(self)
        # Always start locked on both Python 2 and 3
        self._cond = threading.Condition()
        self._value = None
        self._exc = None
        self._callbacks = _weakref.WeakSet()
        self._exception_callbacks = _weakref.WeakSet()

    def ready(self):
        with self._cond:
            return self._exc is None and not self._value is None

    def successful(self):
        return self.ready() and not self._exc

    def __repr__(self):
        if self.ready
