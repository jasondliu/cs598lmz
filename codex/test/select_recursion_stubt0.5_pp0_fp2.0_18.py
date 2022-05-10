import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1

    f = F()
    select.select([f], [], [])
    f.fileno = lambda: None
    select.select([f], [], [])

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 1

    f = F()
    select.select([f], [], [])
    f.fileno = lambda: None
    select.select([f], [], [])

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 1

    f = F()
    select.select([f], [], [])
    f.fileno = lambda: None
    select.select([f], [], [])

def test_select_closed_mutated_3():
    a
