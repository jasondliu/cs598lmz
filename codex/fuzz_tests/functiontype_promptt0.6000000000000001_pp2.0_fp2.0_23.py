import types
# Test types.FunctionType and types.MethodType
def f(x):
    return x + 1

class C(object):
    def method(self, x):
        return x + 2

def test_function():
    assert type(f) is types.FunctionType
    assert type(C.method) is types.MethodType

def test_instancemethod():
    c = C()
    assert type(c.method) is types.MethodType

def test_function_attributes():
    assert f.__name__ == 'f'
    assert f.__doc__ is None
    assert f.__module__ == __name__
    assert f.__dict__ == {}

def test_method_attributes():
    c = C()
    assert c.method.__name__ == 'method'
    assert c.method.__doc__ is None
    assert c.method.__module__ == __name__
    assert c.method.__dict__ == {}

def test_method_attributes2():
    c = C()
    assert C.method.__name__ == 'method'
   
