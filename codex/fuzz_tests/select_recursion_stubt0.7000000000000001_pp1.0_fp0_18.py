import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a.append(F())

    try:
        select.select([], [], a, 1)
    except ValueError:
        pass
    else:
        assert False, 'ValueError not raised'

def test_select_mutated_poll():
    import _testcapi
    if not _testcapi.HAVE_POLL:
        py.test.skip("poll not available")
    a = []

    class F:
        def fileno(self):
            test_select_mutated_poll()
            return a.pop()

    a.append(F())

    try:
        select.poll().poll(0)
    except ValueError:
        pass
    else:
        assert False, 'ValueError not raised'

def test_select_mutated_poll2():
    import _testcapi
    if not _testcapi.HAVE_POLL:
        py.test.skip("poll not available")
    a = []

    class F:
        def fileno(self):
            test_select_
