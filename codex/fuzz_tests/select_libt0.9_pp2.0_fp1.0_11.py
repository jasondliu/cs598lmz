import select
import threading
from contextlib import contextmanager
import time
from collections import namedtuple
from enum import Enum


@dataclass
class SignalAwaiter:
    signal: _cffi_backend.Signal
    coro: asyncio.coroutine
    packed_data: _cffi_backend.PackedData


PendingSignals = collections.defaultdict(set)


# Lists all pending waiters by signal.
#
# Waiting on a signal that is already set will immediately be resolved (all
# waiters will be put into the ready list) without setting PendingSignals.
#
# The queue is locked, hence only one coroutine cares about it at a time.

class NoWaitersException(Exception):
    """Raised when someone tries to clear the signal waiters and there are none.
    """


def remove_waiter(sig):
    waiters = PendingSignals[sig]
    if waiters:
        return waiters.pop()

    # What happens when the waiter is already complete and not in the queue?
    #

