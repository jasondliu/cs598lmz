import types
# Test types.FunctionType
def test_function():
    def f(x):
        return x+1
    assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
def test_builtin_function():
    assert type(abs) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
def test_builtin_method():
    assert type(type.mro) is types.BuiltinMethodType

# Test types.MethodType
def test_method():
    class A:
        def f(self):
            pass
    a = A()
    assert type(a.f) is types.MethodType

# Test types.UnboundMethodType
def test_unbound_method():
    class A:
        def f(self):
            pass
    assert type(A.f) is types.UnboundMethodType

# Test types.ModuleType
def test_module():
    import sys
    assert type(sys) is types.ModuleType

# Test types.TracebackType
def test_traceback():
    try:
        raise Exception

