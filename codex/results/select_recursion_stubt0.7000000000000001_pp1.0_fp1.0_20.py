import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            if len(a) == 0:
                raise ValueError()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_interrupted():
    import os
    import signal

    signal.signal(signal.SIGALRM, lambda signum, frame: None)

    def handler(signum, frame):
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        signal.alarm(0)
        raise OSError(errno.EINTR, os.strerror(errno.EINTR))

    a = []

    class F:
        def fileno(self):
            test_select_interrupted()
            if len(a) == 0:
                raise ValueError()
            return a.pop()

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    try:
        select.select([F()], [], [], None)
    except OSError as e:
        print(
