import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5
    a.append(F())

    try:
        select.select(a, [], [])
    except RuntimeError, e:
        assert str(e) == "I/O operation on closed file"

def test_select_interrupted():
    import os
    import signal

    a = []
    # File descriptors 0, 1, and 2 are already open in CPython,
    # and the OS won't let us close and reopen them.
    fd = os.open("/dev/null", os.O_RDONLY)
    try:
        a.append(fd)
        old_handler = signal.signal(signal.SIGALRM, lambda sig, frm: 1/0)
        try:
            signal.alarm(1)
            try:
                r, w, x = select.select(a, [], [])
            finally:
                signal.alarm(0)
            assert a == r
            assert w == []
            assert x == []
        finally:
            signal.signal(signal.SIGAL
