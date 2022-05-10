import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    assert select.select([f], [], []) == ([], [], [])

def test_select_interrupt():
    a = []
    b = []

    class F:
        def fileno(self):
            a.append(1)
            return b.pop()

    f = F()
    b.append(1)
    b.append(2)
    assert select.select([f], [], []) == ([f], [], [])
    b.append(1)
    b.append(2)
    assert select.select([f], [], []) == ([f], [], [])
