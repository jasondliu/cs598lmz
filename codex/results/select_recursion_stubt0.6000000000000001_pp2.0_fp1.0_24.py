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
    del a[:]
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    a.append(F())
    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    del a[:]
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    a.append(F())
    a.append(F())
    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    del a[:]
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    a.append(F())
    a.append(F())
    a.append(F())
    a.
