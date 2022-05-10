import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    r = select.select([], [], [], 0.1)
    a.append(F())

    try:
        r = select.select([], [], [], 0.1)
        assert 0, "expected error"
    except ValueError:
        pass
    a.append(F())
    try:
        r = select.select([], a, [], 0.1)
        assert 0, "expected error"
    except ValueError:
        pass
    a.append(F())
    try:
        r = select.select([], [], a, 0.1)
        assert 0, "expected error"
    except ValueError:
        pass

    class F:
        def fileno(self):
            return -1

    r = select.select([], [], [], 0.1)
    a.append(F())

    try:
        r = select.select([], [], [], 0.1)
        assert 0, "expected error"
    except ValueError:
        pass
    a.append(F())
   
