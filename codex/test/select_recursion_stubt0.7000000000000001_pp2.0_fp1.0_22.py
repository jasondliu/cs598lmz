import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    fds = list(range(10))
    a.extend(fds)

    select.select([fds[0]], [fds[1]], [fds[2]]) # should work
    select.select([fds[0], F()], [fds[1]], [fds[2]]) # should raise EBADF

def test_select_keyboardinterrupt():
    import signal
    old_handler = signal.signal(signal.SIGINT, signal.default_int_handler)
    try:
        try:
            signal.raise_signal(signal.SIGINT)
        except KeyboardInterrupt as e:
            pass
        select.select([], [], [], 0.01)
    finally:
        signal.signal(signal.SIGINT, old_handler)

