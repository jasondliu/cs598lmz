import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    select.select([f], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    select.select([f], [], [])
    a.pop().close()
    select.select([f], [], [])

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    select.select([f], [], [])
    a.pop().close()
    test_select_mutated()

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    select.select([f], [], [])
    a.pop().close()

