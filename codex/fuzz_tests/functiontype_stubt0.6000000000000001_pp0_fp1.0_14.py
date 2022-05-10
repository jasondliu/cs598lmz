from types import FunctionType
a = (x for x in [1])
print(type(a))
print(FunctionType)
print(type(a) == FunctionType)
print(type(a) is FunctionType)

class A(object):
    pass
print(type(A))
print(type(A) is FunctionType)

a = A()
print(type(a) is A)
print(type(a) == A)
