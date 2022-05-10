import types
# Test types.FunctionType
def f(x):
	return x+1
assert f(5) == 6
assert type(f) is types.FunctionType
# Test types.LambdaType
g = lambda x: x+1
assert g(5) == 6
assert type(g) is types.LambdaType
# Test types.GeneratorType
def h(x):
	yield x
	yield x+1
	yield x+2
assert h(5) == [5,6,7]
assert type(h) is types.GeneratorType
# Test types.ClassType
class A(object):
	pass
assert type(A) is types.TypeType
# Test types.InstanceType
a = A()
assert type(a) is types.InstanceType
# Test types.MethodType
def f(x):
	return x+1
A.f = f
assert type(a.f) is types.MethodType
# Test types.UnboundMethodType
assert type(A.f) is types.UnboundMethodType
# Test types.BuiltinFunctionType
import math
assert
