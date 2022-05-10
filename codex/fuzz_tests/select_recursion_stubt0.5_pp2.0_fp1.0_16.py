import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], a, a, 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1

        def close(self):
            test_select_closed()
            raise ValueError

    f = F()
    f.close()
    select.select([f], a, a, 0)

def test_select_read_error():
    a = []

    class F:
        def fileno(self):
            return 1

        def read(self, n):
            raise ValueError

    f = F()
    select.select([f], a, a, 0)

def test_select_write_error():
    a = []

    class F:
        def fileno(self):
            return 1

        def write(self, s):
            raise ValueError

    f = F()
    select.select(a, [f], a, 0)

def test_select_except_error():
    a = []

    class F:
        def
