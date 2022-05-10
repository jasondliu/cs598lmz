from types import FunctionType
a = (x for x in [1])
b = lambda x : x
c = list.append
d = FunctionType
print type(a)
print type(b)
print type(c)
print type(d)

print type(abs)
print type(lambda x : x)
print type(list)
print type(list.append)

print type(b) == types.FunctionType
print type(c) == types.BuiltinFunctionType
print type(d) == types.TypeType

print type(abs) == types.TypeType
print type(list) == types.TypeType
print type(str) == types.TypeType

print type(dir) == types.BuiltinFunctionType
print type(dir(list)) == types.BuiltinFunctionType
print type(dir(str)) == types.BuiltinFunctionType

print type(abs) == types.LambdaType
print type(lambda x : x) == types.LambdaType
print type(lambda x, y : x + y) == types.LambdaType

print type(b) == types.LambdaType
print type(c
