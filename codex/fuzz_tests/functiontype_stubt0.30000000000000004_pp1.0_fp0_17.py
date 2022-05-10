from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print('='*20)

b = [x for x in [1]]
print(type(b))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, Generator))
print(isinstance(b, FunctionType))

print('='*20)

c = {x for x in [1]}
print(type(c))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))
print(isinstance(c, Generator))
print(isinstance(c, FunctionType))

print('='*20)

d = {x:x for x in [1]}
print(type(d))
print(isinstance(d, Iterator))
print(isinstance(d, Iterable))
print(isinstance(d, Generator))
print(is
