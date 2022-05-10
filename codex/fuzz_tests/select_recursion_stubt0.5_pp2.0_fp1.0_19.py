import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], a, a, 1)

def test_select_closed():
    a = []
    b = []

    class F:
        def fileno(self):
            test_select_closed()
            return 1
        def close(self):
            del b[:]

    select.select([F()], a, a, 1)

def test_select_closed_on_error():
    a = []
    b = []

    class F:
        def fileno(self):
            test_select_closed_on_error()
            raise ValueError
        def close(self):
            del b[:]

    try:
        select.select([F()], a, a, 1)
    except ValueError:
        pass

def test_select_closed_on_error_nonzero():
    a = []
    b = []

    class F:
        def fileno(self):
            test_select_closed_on_error_nonzero()
            raise ValueError
        def close(self):
            del b
