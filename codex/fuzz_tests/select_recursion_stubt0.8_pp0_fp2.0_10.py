import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # XXX: does this happen?
            return a.pop()
    select.select([F()], [], [])

def test_select_invalid_arg():
    try:
        select.select(object(), [], [])
        assert False
    except TypeError:
        pass
    try:
        select.select([], object(), [])
        assert False
    except TypeError:
        pass
    try:
        select.select([], [], object())
        assert False
    except TypeError:
        pass

def test_select_suspend():
    class C:
        def fileno(self):
            sys.suspend_thread()
            raise AssertionError
    try:
        select.select([C()], [], [])
    except RuntimeError:
        pass # expect to be interrupted

def test_select_bad_fd():
    class C:
        def fileno(self):
            return -1
    try:
        select.select([C()], [], [])
    except RuntimeError:
        pass # expect to be interrupted
