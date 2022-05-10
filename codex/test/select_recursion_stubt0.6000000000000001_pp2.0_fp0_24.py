import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[:]

    select.select([F()], [], [])

def test_select_closed():
    class F:
        def fileno(self):
            return -1

    select.select([F()], [], [])

def test_select_closed_mutated():
    a = []

    class F(object):
        def fileno(self):
            test_select_closed_mutated()
            del a[:]
            return -1

    select.select([F()], [], [])

def test_select_closed_mutated2():
    a = []

    class F(object):
        def fileno(self):
            test_select_closed_mutated2()
            del a[:]
            return -1

    select.select([F()], [], [], timeout=None)

def test_select_closed_mutated3():
    a = []

    class F(object):
        def fileno(self):
            test_select_closed_mutated3()
            del a[:]
            return -1
