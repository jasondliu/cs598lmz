import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            a.append(1)
            return ''

    select.select([F()], [], [])

def test_select_mutated_error():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_error()
            return len(a)
        def read(self):
            a.append(1)
            raise OSError

    select.select([F()], [], [])

def test_select_error():
    class F:
        def fileno(self):
            test_select_error()
            return 0
        def read(self):
            return ''

    select.select([F()], [], [])

def test_select_close_fd():
    f = open(__file__)
    def close():
        f.close()
    select.select([f], [], [], 0, close)

def test_select_close_fd_error():
    f = open(__file__)
