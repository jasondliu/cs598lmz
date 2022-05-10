import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select(a, a, a)


# test that a thread can't trigger a deadlock on the signal
# module, by using a lock that is also used by signal handlers.
# This is not an exhaustive test, but it's better than nothing.
# (the problem was that when a thread was interrupted by a signal,
# the signal handler would acquire the lock again before releasing
# it, so the initial acquisition would never be released).

def sleeper(lock, timeout):
    time.sleep(timeout)
    try:
        # As a side effect, this acquires the lock.  This used to
        # deadlock if a signal arrived in the middle of this.
        signal.signal(signal.SIGUSR1, lambda n,f: None)
    finally:
        lock.release()

def alarm_handler(signum, frame):
    raise IOError

def test_signal_lock():
    import _thread
    lock = threading.Lock()
    lock.acquire()
    thread = _thread.
