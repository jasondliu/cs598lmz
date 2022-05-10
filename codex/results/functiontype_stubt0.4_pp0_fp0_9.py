from types import FunctionType
a = (x for x in [1])
print(type(a))

b = [x for x in [1]]
print(type(b))

c = {x for x in [1]}
print(type(c))

d = {x: x for x in [1]}
print(type(d))

e = FunctionType(lambda x: x, globals())
print(type(e))

f = lambda x: x
print(type(f))

g = classmethod(lambda x: x)
print(type(g))

h = staticmethod(lambda x: x)
print(type(h))

# i = memoryview(b'abc')
# print(type(i))

j = type(type)
print(type(j))

k = type(type(type))
print(type(k))

l = type(type(type(type)))
print(type(l))

m = type(type(type(type(type))))
print(type(m))

n = type(type(type(type(type(type)))))
print(type(
