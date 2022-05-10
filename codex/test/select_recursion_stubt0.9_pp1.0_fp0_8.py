import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    while(1):
        a.append(a)
        sys.stderr.write("a: %s\n" % id(a))
        try:
            r, w, x = select.select([F()], [], [], 0.5)
        except OSError:
            pass
        if not a:
            break

def test(selectfunc, testfuncs):
    for f in testfuncs:
        sys.stderr.write("testing %s\n" % f.__name__)
        f(selectfunc)
        sys.stderr.flush()

