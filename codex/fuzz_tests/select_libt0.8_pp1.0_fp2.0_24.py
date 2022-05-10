import select
import sys
import weakref
import logging

_debug = logging.getLogger('concurrent.futures._base').debug

_PENDING = 'PENDING'
_CANCELLED = 'CANCELLED'
_FINISHED = 'FINISHED'

# States a Future can be in.
_STATE_TO_DESCRIPTION_MAP = {
    _PENDING: "Pending",
    _CANCELLED: "Cancelled",
    _FINISHED: "Finished"
}

# Constants returned from Future.cancel().
CANCELLED_AND_NOTIFIED = 1  # The thread executing the callable was cancelled.
CANCELLED_BUT_NOTIFIED = 2  # The thread was cancelled but not yet notified.
NOT_CANCELLED = 3  # The thread was not cancelled.


class Future(object):
    """Represents the result of an asynchronous computation."""

    def __init__(self):
        self._state = _PENDING
        self._result = None
        self._exception = None
