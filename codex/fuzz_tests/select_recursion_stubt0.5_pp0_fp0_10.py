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

def test_select_exception():
    a = []

    class F:
        def fileno(self):
            raise OSError
            return a.pop()

    select.select([F()], [], [])

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()

    select.poll().register(F(), 0)

def test_poll_closed():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.poll().register(F(), 0)

def test_poll_exception():
    a = []

    class F:
        def fileno(self):
            raise
