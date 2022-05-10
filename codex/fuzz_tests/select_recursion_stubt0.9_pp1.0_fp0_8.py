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

if __name__ == "__main__":
    test(select.select, [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9,
                         test10, test11, test12])
    if hasattr(select, 'epoll'):
        test(select.epoll, [test0, test1, test2, test4, test5])
    if hasattr(select
