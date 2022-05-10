import types
# Test types.FunctionType

def f():
    pass

def g(x):
    pass

def h(*args):
    pass

def i(**kwds):
    pass

def j(x, *args, **kwds):
    pass

class C:
    def __init__(self, x):
        pass

def test():
    assert type(f) is types.FunctionType
    assert type(g) is types.FunctionType
    assert type(h) is types.FunctionType
    assert type(i) is types.FunctionType
    assert type(j) is types.FunctionType
    assert type(C.__init__) is types.FunctionType
    assert type(C.__new__) is types.FunctionType
    assert type(type) is types.FunctionType
    assert type(len) is types.FunctionType
    assert type(list.append) is types.FunctionType
    assert type(types.FunctionType) is types.FunctionType
    assert type(test) is types.FunctionType
    assert type(test.__call__) is types.FunctionType

