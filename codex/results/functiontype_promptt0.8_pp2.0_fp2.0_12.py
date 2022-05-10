import types
# Test types.FunctionType
#

def test_functiontype():
    assert isinstance(test_functiontype, types.FunctionType)
    def foo():
        pass
    assert isinstance(foo, types.FunctionType)

# Test types.BuiltinFunctionType
#

def test_builtinfunctiontype():
    import os
    assert isinstance(os.path.join, types.BuiltinFunctionType)
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(test_builtinfunctiontype, types.BuiltinFunctionType)

# Test types.UnboundMethodType
#

# -- class.__init__:
assert isinstance(object.__init__, types.UnboundMethodType)
assert not isinstance(object, types.UnboundMethodType)

# -- class.method:
class A:
    def meth(self):
        pass

assert isinstance(A.meth, types.UnboundMethodType)
assert isinstance(A().meth, types.UnboundMethodType)
assert not isinstance(A, types.UnboundMethodType)
