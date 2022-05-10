import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([F()], [F()], [F()], 1)
    a.append(1)
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def __init__(self):
            self.closed = False
        def fileno(self):
            return 5
        def close(self):
            self.closed = True

    f = F()
    select.select([f], [f], [f], 1)
    a.append(1)
    assert a == [1]
    assert f.closed

def test_select_cannot_close():
    a = []

    class F:
        def __init__(self):
            self.closed = False
        def fileno(self):
            return 5
        def close(self):
            raise ValueError

    f = F()
    select.select([f], [f], [f], 1)
    a.append(1)
    assert a == [1]
    assert f.closed

def test_get_exception
