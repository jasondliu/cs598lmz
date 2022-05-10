import types
# Test types.FunctionType

class T(object):
    def __init__(self):
        self._f = self.f
        self._f2 = types.FunctionType(self._f.func_code, globals(), 'f2')
        self.g2 = types.FunctionType(self._f.func_code, globals(), 'g2')

    def f(self, x):
        return x + 1
    
    def g(self):
        return self


t = T()
assert t._f2(1) == 2
t.g2()
assert t.g2.__name__ == 'g2'

def foo():
    pass
assert types.FunctionType(foo.func_code, globals(), 'bar') is not foo

def foo():
    pass
try:
    types.FunctionType(foo.func_code, {})
except ValueError:
    pass
else:
    assert False, 'Should have raised ValueError'

# Test cell types
x = 3
def foo():
    x = 4
    # x is a closure cell
    assert is
