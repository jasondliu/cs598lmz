import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [])
    test_select_mutated()
    assert a == []

def test_select_interrupted():
    # Test that select() is restarted when interrupted by a signal
    # (see issue #3770).
    import time
    import os
    import signal

    def handler(signum, frame):
        pass

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    time.sleep(2)
    # The following select() used to hang indefinitely.
    select.select([], [], [], 0)
    signal.alarm(0)

def test_select_keyboard_interrupt():
    # Test that select() is interrupted by a signal even without
    # explicitly checking signals (see issue #3770).
    import time
    import os
    import signal

    def handler(signum, frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGALRM, handler)
    signal
