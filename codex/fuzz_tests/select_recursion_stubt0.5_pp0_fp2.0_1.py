import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_error():
    try:
        select.select([], [], [], 1.5)
    except TypeError:
        pass
    else:
        assert False, "didn't raise TypeError"

def test_select_keyboardinterrupt():
    import signal

    def raise_keyboardinterrupt(*args):
        raise KeyboardInterrupt

    signal.signal(signal.SIGALRM, raise_keyboardinterrupt)
    signal.alarm(1)

    try:
        select.select([], [], [], 5)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "didn't raise KeyboardInterrupt"
