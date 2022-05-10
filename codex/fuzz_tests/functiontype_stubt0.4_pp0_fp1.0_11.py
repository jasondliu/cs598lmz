from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

print(issubclass(D, A))
print(issubclass(D, B))
print(issubclass(D, C))
print(issubclass(D, D))
print(issubclass(D, object))

print(isinstance(D, A))
print(isinstance(D, B))
print(isinstance(D, C))
print(isinstance(D, D))
print(isinstance(D, object))

print(isinstance(A, A))
print(isinstance(A, B))

