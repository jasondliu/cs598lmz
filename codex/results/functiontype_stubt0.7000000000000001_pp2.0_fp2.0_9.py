from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(id(a)==id(b))
print(type(a)==type(b))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, type))
print(isinstance(a, object))
print(isinstance(a, set))

print('-------------------------------')

class A():
    pass

a = A()
print(isinstance(a, A))
print(type(a)==A)
print(type(a)==type(A))

print('-------------------------------')

print(isinstance(A, type))
print(type(A))
print(type(object))
