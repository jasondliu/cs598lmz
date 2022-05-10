import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    select.select([F()], [], [], 0)

def test_select_closed_after_timeout():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    select.select([F()], [], [], 1)
