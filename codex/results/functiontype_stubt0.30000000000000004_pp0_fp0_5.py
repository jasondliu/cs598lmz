from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(lambda x: x))

print(type(abs))

print(type(FunctionType))

print(type(FunctionType) == type(lambda x: x))

print(type(FunctionType) == types.FunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type(abs) == types.BuiltinFunctionType)

print(type(x for x in range(10)) == types.GeneratorType)

print(isinstance(x for x in range(10), types.GeneratorType))

print(isinstance(b'a', bytes))

print(isinstance('a', str))

print(isinstance(u'a', str))

print(isinstance(u'a', unicode))

class A(object):
    pass

class B(A):
    pass

print(isinstance(A(), A))

print(type(A()) == A)

print(isinstance(B(), A))

print(type(B
