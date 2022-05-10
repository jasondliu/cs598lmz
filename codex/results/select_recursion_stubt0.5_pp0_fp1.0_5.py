import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    select.select([F()], [], [], 0)
