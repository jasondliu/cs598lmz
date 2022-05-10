fn = lambda: None
# Test fn.__code__.co_varnames
def test_varnames():
    def g():
        pass
    def f(x, y=0):
        return x + y
    def f2(x, y=0):
        a = g()
        return x + y
    class A:
        def __init__(self, x, y=0):
            self.x = x
            self.y = y
        def meth1(self, x, y=0):
            return x + y
        def meth2(self, x, y=0):
            a = g()
            return x + y
    assert fn.__code__.co_varnames == ()
    assert f.__code__.co_varnames == ('x', 'y')
    assert f2.__code__.co_varnames == ('x', 'y')
    assert A.__init__.__code__.co_varnames == ('self', 'x', 'y')
    assert A.meth1.__code__.co_varnames == ('self', 'x',
