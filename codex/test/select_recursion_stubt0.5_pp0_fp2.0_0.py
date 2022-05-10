import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f():
        select.select([F()], [], [])

    try:
        f()
    except IndexError:
        pass
    else:
        assert False, 'select() should have raised IndexError'

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    def f():
        select.select([F()], [], [])

    try:
        f()
    except InterruptedError:
        pass
    else:
        assert False, 'select() should have raised InterruptedError'

def test_select_interrupted_with_timeout():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    def f():
        select.select([F()], [], [], 0.5)

    try:
        f()
    except InterruptedError:
        pass
    else:
        assert False, 'select() should have raised InterruptedError'

