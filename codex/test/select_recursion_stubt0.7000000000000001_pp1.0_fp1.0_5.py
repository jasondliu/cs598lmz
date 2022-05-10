import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(1)
    a.append(2)
    select.select([f], [], [])
    a.append(3)
    a.append(4)
    select.select([f], [], [])

def test_select_return_none():
    class F:
        def fileno(self):
            return None

    f = F()
    assert select.select([f], [], []) == ([], [], [])

def test_select_return_int():
    class F:
        def fileno(self):
            return 1

    f = F()
    assert select.select([f], [], []) == ([f], [], [])

def test_select_return_float():
    class F:
        def fileno(self):
            return 1.5

    f = F()
    assert select.select([f], [], []) == ([f], [], [])

