import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, 'select() should have raised ValueError'

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, 'select() should have raised ValueError'

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a[0] = 1
            return 1

    a.append(F())
    select.select([], [], a)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    a.append(F())
    select
