import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    class S:
        def __init__(self):
            self.f = F()

        def fileno(self):
            return self.f.fileno()

    s = S()
    a.append(1)
    select.select([s], [], [], 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return len(a)

    class S:
        __slots__ = ["f"]

        def __init__(self):
            self.f = F()

        def fileno(self):
            return self.f.fileno()

    s = S()
    a.append(1)
    select.select([s], [], [], 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return len(a)

    class S:
        __slots
