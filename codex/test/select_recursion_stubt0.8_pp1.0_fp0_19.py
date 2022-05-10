import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    try:
        select.select(a, [], [])
    except RuntimeError:
        pass
    else:
        assert 0, "RuntimeError expected"

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            a.pop()
    a.append(F())
    try:
        select.select(a, [], [])
    except IndexError:
        pass
    else:
        assert 0, "IndexError expected"

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            del a[0]
    a.append(F())
    try:
        select.select(a, [], [])
    except IndexError:
        pass
    else:
        assert 0, "IndexError expected"

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            raise ValueError
