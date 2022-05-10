import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())
    try:
        select.select([], a, [])
    except RuntimeError:
        pass
    else:
        raise AssertionError("select() didn't raise RuntimeError")

def test_select_mutated_2():
    # Issue #18073: select() should not crash when the list of file objects
    # is mutated during the select() call.
    a = []

    class F:
        def fileno(self):
            a.append(F())
            return 1
    a.append(F())
    try:
        select.select([], a, [])
    except RuntimeError:
        pass
    else:
        raise AssertionError("select() didn't raise RuntimeError")

def test_select_mutated_3():
    # Issue #18073: select() should not crash when the list of file objects
    # is mutated during the select() call.
    a = []

    class F:
        def fileno(self):
            del a[:]
            return 1
    a
