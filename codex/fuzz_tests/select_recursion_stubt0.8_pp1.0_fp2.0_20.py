import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(1)

    f = F()
    select.select([f], [f], [f], 0)

    assert a == [1]

class TestSelect(object):
    def test_select(self):
        def foo(wlist, xlist, ylist, timeout):
            return wlist, xlist, ylist, timeout
        select.select = foo
        assert select.select([], [], [], 5) == ([], [], [], 5)

    def test_error(self):
        import errno
        class MyIO(object):
            def fileno(self):
                return 1
            def close(self):
                pass
        io = MyIO()
        try:
            select.select([io], [], [], 0)
        except select.error as e:
            assert e.errno == errno.EBADF
        else:
            assert 0, "should have raised"

class AppTestSelect:
    spaceconfig = dict(usemodules=('select',))

    def
