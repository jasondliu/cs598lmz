from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == types.FunctionType)

print(type(a.__iter__) == types.MethodType)
print(type(a.__iter__) == types.BuiltinMethodType)
print(type(a.__iter__) == types.BuiltinFunctionType)

print(type(a.__iter__) == types.GeneratorType)
print(type(a.__iter__) == types.GeneratorType)

print(type(a.__iter__) == types.TracebackType)
print(type(a.__iter__) == types.FrameType)
print(type(a.__iter__) == types.CodeType)
print(type(a.__iter__) == types.
