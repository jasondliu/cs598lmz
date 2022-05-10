import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def readinto(self, b):
            assert b is a

    f = F()

    try:
        select.select([f], [], [], 1)
    except ValueError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
        def readinto(self, b):
            assert b is a

    try:
        select.select([], [F()], [], 1)
    except ValueError:
        pass
