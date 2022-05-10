import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append(1)
            return 1

    f = F()
    select.select([f], [], [], 1)
    assert a

def test_select_read():
    a = []

    class F:
        def __init__(self, l):
            self.l = l

        def fileno(self):
            test_select_read()
            return 0

        def read(self, size):
            return self.l.pop(0).read(size)

    f = F([io.BytesIO(b'x'), io.BytesIO(b'y')])
    select.select([f], [], [], 0)
    assert a == [1]

def test_select_read_mutate():
    a = []

    class F:
        def __init__(self, l):
            self.l = l

        def fileno(self):
            test_select_read_mutate()
            return 0

        def read(self, size):
            a.append(1)
