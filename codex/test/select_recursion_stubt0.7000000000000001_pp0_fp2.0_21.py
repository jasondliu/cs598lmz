import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    class G:
        def fileno(self):
            return a.pop()

    s = select.select([F(), G()], [], [])
    assert not s[0]

def test_select_error():
    class F:
        def fileno(self):
            return _testcapi.INT_MAX + 1
    raises(OverflowError, select.select, [F()], [], [])

def test_select_bad_list():
    raises(TypeError, select.select, 42, [], [])
    raises(TypeError, select.select, [], 42, [])
    raises(TypeError, select.select, [], [], 42)


def _make_bad_fd():
    import os
    fd = _testcapi.INT_MAX + 1
    if hasattr(os, 'closerange'):
        os.closerange(fd, fd+1)
