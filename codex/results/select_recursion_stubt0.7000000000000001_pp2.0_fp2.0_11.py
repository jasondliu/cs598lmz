import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())

    select.select([f], [], [], 0)

    test_select_mutated()


class Simple:
    def fileno(self):
        return 5

class Functional:
    def __init__(self, fileno):
        self.fileno = fileno

class FunctionalFail:
    def __init__(self, fileno):
        self.fileno = fileno
    def __repr__(self):
        raise RuntimeError

class Bad:
    def fileno(self):
        return 'fileno'

class BadMethod:
    def read(self):
        return 'read'

class BadGetattr:
    def __getattr__(self, attr):
        if attr == 'fileno':
            return 'fileno'
        raise AttributeError

class BadClose:
    def fileno(self):
        return 5
    def close(self):
        raise IOError

class BadEnter:
    def fileno
