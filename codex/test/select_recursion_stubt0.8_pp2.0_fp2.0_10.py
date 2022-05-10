import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def read(self):
            a.append(self)
            raise BlockingIOError

    f = F()
    try:
        select.select([f], [], [])
    except InterruptedError:
        pass
    assert a == [f]


def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1

        def close(self):
            a.append(self)
            return 0

    f = F()
    select.select([f], [], [])
    assert a == [f]


class BadSocket:
    def __init__(self, s):
        test_select_mutated()
        self.s = s

    def fileno(self):
        return self.s

    def read(self):
        raise BlockingIOError

    def close(self):
        return 0


