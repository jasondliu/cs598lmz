import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    select.select([f], [], [f], 1)

def test_select_remove():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    select.select([f], [], [f], 1)

def test_select_remove_strict():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    select.select([f], [], [f], 1)
