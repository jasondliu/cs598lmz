import weakref

import _thread

class _reentrant_lock:
    """\
    A reentrant lock object.
    """

    def __init__(self):
        self._lock = _thread.allocate_lock()
        self._locked = 0
        self._owner = None

    def acquire(self, wait=1):
        """\
        Acquire a lock.

        @param wait: If True, wait until the lock is acquired. If
            False, return immediately.
        @return: True if the lock was acquired, False if it was not
            acquired and wait was False.
        """
        me = _thread.get_ident()
        result = 0
        if self._owner is me:
            self._locked = self._locked + 1
            result = 1
        elif not self._lock.locked() or wait:
            self._lock.acquire()
            self._locked = 1
            self._owner = me
            result = 1
        return result

    def release(self):
        """\
        Release a lock.
        """
