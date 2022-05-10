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
            a.pop().close()
            return 1

    select.select([F()], [], [])

def test_select_closed_after_wait():
    a = []

    class F:
        def fileno(self):
            return 1

    select.select([F()], [], [])
    a.pop().close()

def test_select_closed_before_wait():
    a = []

    class F:
        def fileno(self):
            return 1

    a.pop().close()
    select.select([F()], [], [])

def test_select_closed_after_wait_with_timeout():
    a = []

    class F:
        def fileno(self):
            return 1

    select.select([F()], [], [], 0.1)
    a.pop().close()

