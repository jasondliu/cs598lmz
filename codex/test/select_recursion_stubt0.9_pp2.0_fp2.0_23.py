import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del rec[0]
            return 0

    F().fileno()
    rec = [1]
    select.select([], [F()], [])

def test_select_mutated2():
    SOCKET_ERROR = getattr(select, 'SOCKET_ERROR', 0)
    s = socket.socket()
    s.fileno = lambda: 1
    class X:
        def fileno(self):
            del rec[0]
            raise SOCKET_ERROR
    rec = [1]
    try:
        select.select([], [X()], [])
    except IndexError:
        pass
    s.close()

def test_deadlock():
    # Make sure the GC interrupter doesn't get into a deadlock when another
    # thread is blocked in poll() without a timeout.
    import threading
    import os

    r, w = os.pipe()
    flags = fcntl.fcntl(r, fcntl.F_GETFL)
