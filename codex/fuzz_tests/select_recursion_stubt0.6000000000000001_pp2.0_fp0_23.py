import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_interrupted():
    import errno
    import os
    import signal

    def handler(ignored):
        pass
    signal.signal(signal.SIGALRM, handler)
    try:
        signal.alarm(1)
        try:
            select.select([], [], [], 2)
        except select.error as e:
            assert e.args[0] == errno.EINTR
            assert e.args[1] == os.strerror(errno.EINTR)
        else:
            assert False, "expected EINTR"
    finally:
        signal.alarm(0)

def test_select_timeout():
    import time
    now = time.time()
    select.select([], [], [], 0.5)
    assert time.time() - now >= 0.5

def test_select_timeout_is
