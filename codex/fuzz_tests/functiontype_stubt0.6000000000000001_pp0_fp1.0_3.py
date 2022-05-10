from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

a = {'a': 1}
print(isinstance(a, dict))
print(isinstance(a, dict))
print(isinstance(a, dict))
print(isinstance(a, dict))
print(isinstance(a, dict))
print(isinstance(a, dict))
print(isinstance(a, dict))

print(type(a))
print(type(a) == dict)

print(type(a) is dict)

class A:
    pass

class B(A):
    pass

print(isinstance(B(), A))

class C:
    pass

print(issubclass(B, A))
print(issubclass(B, C))

print(isinstance(B, A))
print(isinstance(B, C))

print(isinstance(B(), C))
print(isinstance(B, C))

print(issubclass(B, B))

class
