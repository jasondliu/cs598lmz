import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    fd = f.fileno()
    assert fd == 0 or fd == 1
    assert f.fileno() == fd
    select.select([f], [f], [f], 0)


def test_regression_1():
    # bug: calling fileno *at all* makes the object invalid.
    # this test should succeed, but it segfaults in CPython
    class F:
        def fileno(self):
            return 123

    f = F()
    assert f.fileno() == 123
    select.select([f], [f], [f], 0)
    assert f.fileno() == 123


def test_regression_2():
    # bug: calling fileno on an object, using it as a file descriptor,
    # then calling fileno on it again, is not allowed.
    class F:
        def fileno(self):
            assert False, "fileno() should only be called once"

    f = F()
    select.select([f], [f], [
