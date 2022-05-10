import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    a.append(F())
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0
    a.append(F())
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return 0
    a.append(F())
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return 0
   
