from types import FunctionType
a = (x for x in [1])
b = [1]
c = {'a': 1}
d = 'abc'
e = 1
f = FunctionType(lambda: None, globals())
g = True
h = bytes([1])
i = b'abc'
j = bytearray([1])
k = range(10)
l = memoryview(b'abc')
m = object()

for x in a, b, c, d, e, f, g, h, i, j, k, l, m:
    print(type(x), isinstance(x, Iterable), isinstance(x, Iterator))

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

a = (x for x in [1])
b = [1]
c = {'a': 1}
d = 'abc'
e = 1
f = FunctionType(lambda: None, globals())
g = True
h = bytes([1])
i = b'abc'
j = bytearray([1])
k = range(10)
l = memory
