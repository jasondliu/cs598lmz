import weakref

from .utils import is_transaction_pending, time, time_monotonic


class Transaction(object):
    __slots__ = ("_completion_time", "_creation_time", "_finish_time", "_id",
                 "_request", "_status", "_status_message", "_token")

    _COMMIT_TIMEOUT = 2
    _ROLLBACK_TIMEOUT = 1

    def __init__(self):
        self._completion_time = None
        self._creation_time = None
        self._finish_time = None
        self._id = None
        self._request = None
        self._status = None
        self._status_message = None
        self._token = None

    @property
    def finished(self):
        return self._finish_time is not None

    @property
    def commit_time(self):
        return self._COMMIT_TIMEOUT

    @property
    def id(self):
        return self._id

    @property
    def pending(self):
        return is_transaction_pending(self._
