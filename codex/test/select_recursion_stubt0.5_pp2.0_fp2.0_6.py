import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f)
    r = select.select([f], [], [])
    assert r == ([f], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    a.append(f)
    r = select.select([f], [], [])
    assert r == ([], [], [])

def test_select_closed_early():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    a.append(f)
    # it's not clear that this is the right behaviour
    r = select.select([f], [], [], 0)
    assert r == ([], [], [])

class MyFile(object):
    def __init__(self, data):
        self.data = data
        self.pos = 0

