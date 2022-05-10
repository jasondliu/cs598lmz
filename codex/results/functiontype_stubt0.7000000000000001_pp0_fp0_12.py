from types import FunctionType
a = (x for x in [1])
print(type(a))

b = [x for x in [1]]
print(type(b))

c = {x for x in [1]}
print(type(c))

d = {'a': x for x in [1]}
print(type(d))

f = FunctionType(lambda: 1, {})
print(type(f))

print(type(None))

print(type(set()))

print(type(list()))

class A(object):
    pass

print(type(A))

a = A()
print(type(a))
