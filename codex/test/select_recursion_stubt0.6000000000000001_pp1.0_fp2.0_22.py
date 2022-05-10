import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [0]
    select.select([f], [], [])
    a = [1]
    select.select([f], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a = [0]
    select.select([f], [], [])
    a = [1]
    select.select([f], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a = [0, 1]
    select.select([f], [], [])
    a = [1]
    select.select([f], [], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
