import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "didn't raise ValueError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1
        def close(self):
            a.append(1)
            raise ValueError

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "didn't raise ValueError"
    assert a == [1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 1
        def close(self):
            test_select_closed_mutated()
            a.append(1)
            raise ValueError

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
       
