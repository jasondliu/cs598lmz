import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 999

    x = [F() for i in range(200)]
    a[:] = x
    a[:] = (y for y in x)
    a[:] = (x if x else y for y in x)
    a[:] = (x+y for y in x)
    a[:] = (x.fileno() for y in x)
    select.select(a, a, a)

def test_select_bad_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_bad_mutated()
            return 999

    x = [F() for i in range(200)]
    a[:] = (y for y in x)
    a[:] = (x if x else y for y in x)
    a[:] = (x+y for y in x)
    a[:] = (x.fileno() for y in x)
    a[:] = x
    try:
        select.select(a, a, a)
    except RuntimeError as exc:
        if '
