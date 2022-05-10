import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            # Using del breaks on py3 (3.1, 3.2) and PyOS_InputHook
            # workaround (3.3).
            a[:] = []
            return 1

        def readline(self):
            return b"\r\n"

    f = F()
    a.append(f)
    for _ in range(1, 300):
        select.select([f], [], [])


def test_select_wake_up():
    # Issue #14585: Make all error events on a file descriptor
    # mutually exclusive, to avoid interpreting an event posted by
    # select() as if it were posted by the I/O completion routines.
    c1, c2 = socket.socketpair()
    try:
        select.select([c1], [], [])
        c1.shutdown(socket.SHUT_RDWR)
        for i in range(100):
            # Should not hang
            select.select([c2], [], [])
    finally:
        c1.close()
        c2.close()

def test_
