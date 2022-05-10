import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())

    try:
        select.select(a, a, a)
    except RuntimeError as e:
        assert "object mutated" in str(e)
    else:
        assert False

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    a.append(F())

    try:
        select.select(a, a, a)
    except RuntimeError as e:
        assert "object mutated" in str(e)
    else:
        assert False

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    a.append(F())

    select.select(a, a, a) # doesn't raise

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    a
