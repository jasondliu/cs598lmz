import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    assert select.select([F()], [], [], 0) == ([], [], [])
    assert select.select([], [], [], 0) == ([], [], [])
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "did not raise ValueError"

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            return 0

    def handler(signum, frame):
        a.append(signum)

    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(1)
        assert select.select([F()], [], [], 2) == ([], [], [])
        assert a == [signal.SIGALRM]
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

