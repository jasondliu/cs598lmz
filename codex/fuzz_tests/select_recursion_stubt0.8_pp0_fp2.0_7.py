import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    select.select([F()], [], [], -1)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop(0)

    select.select([F()], [F()], [], -1)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop(0)

    select.select([F()], [], [F()], -1)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return a.pop(0)

    select.select([F()], [F()], [F()], -1)


def test_select_throw():
    class F:
        def fileno(self):
            raise OSError


