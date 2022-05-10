import types
# Test types.FunctionType
def test_function():
    def func(a, b):
        return a + b
    assert func(1, 2) == 3
    assert isinstance(func, types.FunctionType)

# Test types.MethodType
def test_method():
    def func(a, b):
        return a + b
    class A:
        def __init__(self):
            self.a = 0
            self.b = 0
            self.c = 0
        def method(self, a, b):
            self.a = a
            self.b = b
            self.c = a + b
    a = A()
    a.method(1, 2)
    assert a.c == 3
    a.m1 = types.MethodType(func, a, A)
    assert a.m1(3, 4) == 7

# Test types.BuiltinFunctionType
def test_builtin_function():
    assert isinstance(abs, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
def test_builtin_method():
    assert
