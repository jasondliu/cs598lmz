import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], a, a, 0)

def test_select_error_2():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F(), F()], a, a, 0)

def test_select_error_3():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F(), F()], a, a, 0)

def test_select_error_4():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F(), F()], a, a, 0)

def test_select_error_5():
    a = []

    class F:
        def fileno(self):
            return 0

