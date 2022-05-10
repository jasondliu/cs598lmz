import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([F()], [], [], 0)
    assert len(s) == 3

def test_select_error():
    s = select.select([], [], [], 0)
    assert len(s) == 3
