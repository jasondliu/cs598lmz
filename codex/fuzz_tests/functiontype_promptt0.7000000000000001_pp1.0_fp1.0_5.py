import types
# Test types.FunctionType

def f1(): pass
def f2(a): pass
def f3(a, *b): pass
def f4(a, **b): pass
def f5(a, *b, **c): pass
def f6(a, b=2): pass
def f7(a, b=2, *c): pass
def f8(a, b=2, **c): pass
def f9(a, b=2, *c, **d): pass
def f10(a, b, c=3, d=4): pass

def test(f, nargs):
    fn = types.FunctionType(f.__code__, f.__globals__, f.__name__,
                            f.__defaults__, f.__closure__)
    assert fn.__code__ is f.__code__
    assert fn.__globals__ is f.__globals__
    assert fn.__name__ == f.__name__
    assert fn.__defaults__ == f.__defaults__
    assert fn.__closure__ ==
