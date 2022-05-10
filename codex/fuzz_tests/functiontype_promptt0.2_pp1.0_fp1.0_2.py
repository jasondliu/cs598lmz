import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType
# Test types.GeneratorType
def h(): yield 1
assert type(h()) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(g.__code__) is types.CodeType
assert type(h.__code__) is types.CodeType
# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) is types.MethodType
assert type(C().m) is types.MethodType
# Test types.UnboundMethodType
assert type(C.m) is types.UnboundMethodType
# Test types.BuiltinMethodType
assert type(len) is types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.ModuleType
import sys
assert type(
