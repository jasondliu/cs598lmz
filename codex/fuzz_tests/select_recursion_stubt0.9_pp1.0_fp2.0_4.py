import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([], a, a)
    except IndexError:
        pass
    a.append(F())
    try:
        select.select([], a, a)
    except RuntimeError:
        pass
    else:
        print('Should have raised')

def test_select_racing():
    class F:
        def fileno(self):
            test_select_racing()
            return 0

    for _ in range(1024):
        r = [F()]
        w = [F()]
        x = [F()]
        try:
            select.select(r, w, x)
        except RuntimeError:
            pass
        else:
            print('Should have raised')

def test_select_racing2():
    # Regression test for the issue with select() and the garbage collector
    # reported on python-dev mailing list by Raymond Hettinger; see
    # http://mail.python.org/pipermail/python-dev/2007-September/073757.html.
    import weak
