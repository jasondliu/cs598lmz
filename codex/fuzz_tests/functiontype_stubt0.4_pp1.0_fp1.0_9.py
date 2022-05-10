from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

b = FunctionType
print(isinstance(b, FunctionType))

c = lambda x: x
print(isinstance(c, FunctionType))

d = type(lambda x: x)
print(d)

e = type(type)
print(e)

f = type(isinstance)
print(f)

g = type(FunctionType)
print(g)

h = type(FunctionType())
print(h)

i = type(FunctionType)
print(i)

j = type(FunctionType())
print(j)

k = type(FunctionType)
print(k)

l = type(FunctionType())
print(l)

m = type(FunctionType)
print(m)

n = type(FunctionType())
print(n)

o = type(FunctionType)
print(o)

p = type(FunctionType())
print(p)

q = type(FunctionType)
print(q)

r = type(FunctionType())
print
