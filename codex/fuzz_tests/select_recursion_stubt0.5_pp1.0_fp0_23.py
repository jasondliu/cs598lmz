import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def __call__(self):
            a.append(1)

    select.select([F()], [], [])

def test_select_interrupted():
    import signal
    import time
    import os
    def handler(signum, frame):
        pass
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    time.sleep(2)
    signal.alarm(0)
    try:
        select.select([], [], [], 0.1)
    except select.error as e:
        assert e.args[0] == errno.EINTR
    else:
        assert False, "select() not interrupted by a signal"

def test_select_error():
    import time
    import errno
    try:
        time.sleep(1)
        select.select([], [], [], 0.1)
    except select.error as e:
        assert e.args[0] == errno.EINTR
    else:
        assert False,
