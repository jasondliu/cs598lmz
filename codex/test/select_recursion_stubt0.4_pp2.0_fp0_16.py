import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], a, a)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            raise ValueError

    select.select([F()], a, a)

def test_select_error_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_error_mutated()
            raise ValueError

    select.select([F()], a, a)

def test_select_error_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_error_mutated2()
            return 1

    select.select([F()], a, a)

def test_select_error_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_error_mutated3()
            return 1

    select.select([F()], a, a)

