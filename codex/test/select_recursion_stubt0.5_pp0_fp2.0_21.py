import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_overflow():
    a = []

    class F:
        def fileno(self):
            test_select_overflow()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            test_select_error()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_error_2():
    a = []

    class F:
        def fileno(self):
            test_select_error()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_error_3():
    a = []

    class F:
        def fileno(self):
            test_select_error()
