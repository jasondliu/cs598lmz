import gc, weakref
from collections import UserDict
import sqlite3
from contextlib import contextmanager
from multiprocessing import Queue
import threading
import queue

__all__ = ['transact', 'Transaction', 'TransactionOpts']


def _to_dict(l):
    d = {}
    for (a, b) in l:
        b = (0,0,0) if b is None else b
        d[a] = b
    return d


class _Cache(UserDict):
    def __init__(self, memsize):
        UserDict.__init__(self, {})
        self._size = memsize
        self._hitg = 0
        self._hitn = 0
        self._missg = 0
        self._missn = 0
        self._q = queue.Queue(maxsize=memsize)

    def __contains__(self, k):
        if k in self.data:
            self._hitg += 1
            self._hitn += len(self.data[k])
            return True
