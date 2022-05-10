import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = select.select([F()], a, a, 0)
    assert s == ([], [], []), s


def test_select_keyboardinterrupt():
    try:
        for i in range(100):
            select.select([], [], [], 1e-1)
    except KeyboardInterrupt:
        pass
    else:
        raise Exception("did not raise")
