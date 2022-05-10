from types import FunctionType
a = (x for x in [1])
b = [1,2]

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(b, Iterator))
print('--------------------')

class A:
    def __init__(self, a):
        print(a)

a = A(1)
print(isinstance(a, A))
print(isinstance(A, type))
print(isinstance(A, FunctionType))
print(isinstance(a, object))
print('--------------------')

class B(object):
    pass

b = B()

print(isinstance(B, type))
print(isinstance(b, B))
print(isinstance(b, object))
