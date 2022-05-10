import types
# Test types.FunctionType
def foo(x, y):
    return x * y

def test_function():
    assert type(foo) is types.FunctionType
    assert type(foo) is types.FunctionType
    
# Test types.MethodType
class A(object):
    def bar(self, x):
        return 2*x

def test_method():
    assert type(A.bar) is types.MethodType
    assert type(A().bar) is types.MethodType

# Test types.BuiltinFunctionType
def test_builtin_function():
    assert type(len) is types.BuiltinFunctionType
    assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
def test_builtin_method():
    assert type([].append) is types.BuiltinMethodType
    assert type([].append) is types.BuiltinMethodType

# Test types.ModuleType
def test_module():
    import sys
    assert type(sys) is types.ModuleType
    assert type(sys) is types.ModuleType

# Test types.Tr
