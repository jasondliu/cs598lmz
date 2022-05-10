from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))

def test():
    pass

print(type(test))
print(type(test) == FunctionType)
print(isinstance(test, FunctionType))

class A:
    pass

a = A()
print(type(a))
print(type(A))

print(type(a) == A)
print(isinstance(a, A))
print(isinstance(A, type))

print(isinstance(a, type))
print(isinstance(A, object))
