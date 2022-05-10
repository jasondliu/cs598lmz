import types
# Test types.FunctionType
import sys
import types
def f(): pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType or type(f) == types.FunctionType
assert sys.getrefcount(f) == 2
# Test types.LambdaType
f = lambda: None
assert type(f) == types.LambdaType
assert type(f) == types.FunctionType
# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) == types.MethodType
assert type(C().f) == types.MethodType
# Test types.BuiltinMethodType
class C:
    def f(self): pass
assert type(list.append) == types.BuiltinMethodType
assert type(C.f) == types.MethodType
# Test types.UnboundMethodType
assert type(C.f) == types.MethodType
assert type(C.f) == types.UnboundMethodType
# Test types.CodeType
def f(): pass
assert type(f.func_code) == types.CodeType

