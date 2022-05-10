from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(isinstance(a, tuple))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, str))
print(isinstance(a, (str, tuple)))
print(isinstance(a, (str, tuple, GeneratorType)))

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

print(isinstance(123, int))
print(isinstance(123, (int, float, str)))
print(isinstance('123', str))
print(isinstance('123', (int, float, str)))
print(isinstance('123', (int, float, str, bytes)))
print(isinstance(b'123', (int, float, str, bytes)))
print(isinstance(
