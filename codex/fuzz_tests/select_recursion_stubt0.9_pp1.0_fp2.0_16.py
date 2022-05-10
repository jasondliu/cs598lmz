import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2

        def poll(self): # On PyPy, poll is the entry point
            a.append(self)
            return 0

    testmod = imp.new_module("test")
    testmod.F = F
    sys.modules["test"] = testmod
    try:
        select.select([F()], [], [])
    except ImportError:
        py.test.skip("cannot import select module")

    assert a == [F()]

class TestW_SelectObject:
    def setup_method(self, method):
        self.w_select = space.appexec([], """():
        import select
        return select""")

    def test_select(self):
        import select

        l = []

        class Fds(object):
            def __init__(self, n):
                self.n = n
                self.i = 0
            def __iter__(self):
                return self
            def __next__(self):
                if self.i < self.n:
                    self.i += 1
                    return sys.st
