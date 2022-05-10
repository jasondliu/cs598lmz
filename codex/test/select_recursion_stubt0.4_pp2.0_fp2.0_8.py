import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.select([F()], [], [])

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_bad_file():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.select([F()], [], [])

def test_select_bad_file_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_bad_file_mutated()
            return a.pop()

    select.select([F()], [], [])

