import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(1)

    s = select.int_types[0](0)
    select.select([s], [], [])
    f = F()
    select.select([f], [], [])
    try:
        select.select([f], [], [], 1)
    except KeyboardInterrupt:
        pass

def test_select_except():
    s = select.int_types[0](0)
    select.select([s], [], [])
    # calling into pure Python should have no effect on pending
    # exceptions:  calling pure Python raises an exception, then the
    # pure Python call ends, and the exception is pending
    l = []
    def func(x):
        l.append(x)
    try:
        select.select([s], [], [])
    except Exception:
        func(sys.exc_info()[0])
    import StringIO
    StringIO.StringIO()
    assert l[0] is not None

