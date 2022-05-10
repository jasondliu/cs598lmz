import types
# Test types.FunctionType:
def f(x): return x
def g(f, x): return f(x)
def h(x): return g(f, x)
res = h(1)
assert res == 1
class A:
    "Example class."
    x = 3
    def f(self, y): return self.x + y
def test_class():
    o = A()
    assert o.f(2) == 5
    assert o.f(self=o, y=2) == 5

def test_function_attributes():
    def f():
        pass
    assert f.__name__ == "f"
    assert f.__doc__ == None
    def g():
        "hello"
        pass
    assert g.__name__ == "g"
    assert g.__doc__ == "hello"
    def f(a, b, c, d=1, e=2, f=3):
        pass
    assert f.__defaults__ == (1,2,3)
    def g(a, b, c, d=1, e=2
