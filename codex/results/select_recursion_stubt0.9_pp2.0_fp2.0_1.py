import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[:]
            #(exit the function)

    def f():
        select.select([F()], [], [])
    assert_raises(ValueError, f)
    a.append(1)

# interp-level function
def test_select_iterable():
    class F:
        def fileno(self):
            return 1
    fds = [F()]
    assert select.select(fds, fds, fds, 1) == ([F()], [F()], [F()])

class TestSelect(_testcapi.BaseTestCheckErrors):
    def setup_class(cls):
        _testcapi.BaseTestCheckErrors.setup_class.im_func(cls)
        cls.space = gettestobjspace(usemodules=('select',))

    def test_select_argcheck(self):
        space = self.space
        select_module = space.getbuiltinmodule('select')
        w_x = space.wrap(20)
        w_y = space.wrap(20.0)
