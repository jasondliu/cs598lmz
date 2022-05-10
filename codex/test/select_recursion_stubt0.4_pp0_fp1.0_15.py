import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()

    select.select([f], [], [])
    a.append(1)
    select.select([f], [], [])
    a.append(2)
    select.select([f], [], [])
    a.append(3)

    assert a == [1, 2, 3], a

def test_select_keyboardinterrupt():
    import signal
    import os

    def handler(signum, frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)

    try:
        select.select([], [], [])
    except KeyboardInterrupt:
        pass
    else:
        assert False, "Did not raise"

    signal.alarm(0)
