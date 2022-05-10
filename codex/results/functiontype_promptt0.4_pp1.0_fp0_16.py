import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType
# Test types.GeneratorType
def h():
    yield 1
assert type(h()) is types.GeneratorType
# Test types.ClassType
class A:
    pass
assert type(A) is types.ClassType
# Test types.InstanceType
a = A()
assert type(a) is types.InstanceType
# Test types.MethodType
assert type(A.__init__) is types.MethodType
assert type(a.__init__) is types.MethodType
# Test types.UnboundMethodType
assert type(A.__init__) is types.UnboundMethodType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType
# Test
