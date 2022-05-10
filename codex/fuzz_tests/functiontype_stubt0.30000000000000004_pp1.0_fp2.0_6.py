from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == types.FunctionType)
print(type(a.__iter__) == types.BuiltinFunctionType)
print(type(a.__iter__) == types.MethodType)
print(type(a.__iter__) == types.BuiltinMethodType)

print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)
print(type(a.__next__) == types.BuiltinFunctionType)
print(type(a.__next__) == types.MethodType)
print(type(a.__next__) == types.BuiltinMethodType)

print(type(a.send))
print(type(a.send) == FunctionType)
print(type(a.send) == types.FunctionType)
print(type(a.send) == types.Built
