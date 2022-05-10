import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
def f(): pass
def g(): pass
assert not isinstance(g, types.FunctionType)
# Test types.BuiltinFunctionType
def f(): pass
assert isinstance(f, types.BuiltinFunctionType)
def f(): pass
assert not isinstance(f, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
def f(): pass
assert isinstance(f.__call__, types.BuiltinMethodType)
def f(): pass
assert not isinstance(f.__call__, types.BuiltinMethodType)
# Test types.MethodType
def f(): pass
assert not isinstance(f, types.MethodType)
def f(): pass
class C:
    def g(self): pass
assert isinstance(f, types.MethodType)
# Test types.UnboundMethodType
def f(): pass
assert isinstance(f, types.UnboundMethodType)
def f(): pass
class C:
    def g(self): pass
assert isinstance(f, types.UnboundMethod
