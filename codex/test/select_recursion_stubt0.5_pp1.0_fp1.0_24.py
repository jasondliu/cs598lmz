import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"

def test_select_closed_in_callback():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"

def test_select_closed_in_callback2():
    a = []

