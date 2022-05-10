import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()

    a = [1]
    fd = f.fileno()
    assert fd == 1

    a = [2]
    fd = f.fileno()
    assert fd == 2

    a = []
    try:
        f.fileno()
    except IndexError:
        pass
    else:
        raise AssertionError("did not raise")

def test_select_two_objects():
    class F:
        def fileno(self):
            return 1

    f = F()
    fd = f.fileno()
    assert fd == 1
