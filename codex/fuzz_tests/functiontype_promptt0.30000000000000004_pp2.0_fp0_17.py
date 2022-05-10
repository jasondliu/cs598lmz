import types
# Test types.FunctionType
def foo():
    pass

def bar():
    pass

def baz():
    pass

def test_types_functiontype():
    assert isinstance(foo, types.FunctionType)
    assert isinstance(bar, types.FunctionType)
    assert isinstance(baz, types.FunctionType)

# Test types.BuiltinFunctionType
def test_types_builtinfunctiontype():
    assert isinstance(len, types.BuiltinFunctionType)
    assert isinstance(min, types.BuiltinFunctionType)
    assert isinstance(max, types.BuiltinFunctionType)

# Test types.MethodType
class Foo(object):
    def bar(self):
        pass

def test_types_methodtype():
    assert isinstance(Foo.bar, types.MethodType)
    assert isinstance(Foo().bar, types.MethodType)

# Test types.BuiltinMethodType
def test_types_builtinmethodtype():
    assert isinstance(Foo.__init__, types.BuiltinMethodType)
    assert isinstance(Foo
