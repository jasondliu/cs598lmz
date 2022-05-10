from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = {1: 1}
e = 1
f = 1.0
g = '1'
h = b'1'
i = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

# isinstance
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))
print(isinstance(d, Iterator))
print(isinstance(e, Iterator))
print(isinstance(f, Iterator))
print(isinstance(g, Iterator))
print(isinstance(h, Iterator))
print(isinstance(i, Iterator))

# dir
print(dir(a))
print(dir(b))
print(dir(c))
print(dir(d))
print(dir(e))

