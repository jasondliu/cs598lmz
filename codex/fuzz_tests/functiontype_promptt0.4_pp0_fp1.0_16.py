import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
import sys
assert isinstance(sys.exit, types.BuiltinFunctionType)
assert not isinstance(sys.exit, types.FunctionType)
# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.FunctionType)
# Test types.GeneratorType
def g(): yield 1
assert isinstance(g, types.GeneratorType)
assert not isinstance(g, types.FunctionType)
# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.FunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert not isinstance(list.append, types.MethodType)

# Test types.Un
