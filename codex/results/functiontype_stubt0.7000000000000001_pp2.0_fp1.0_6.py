from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = {'a':1}
e = 'abc'
f = FunctionType(lambda x:x,globals())
g = type
h = 1

print(isgeneratorfunction(a))
print(isgeneratorfunction(b))
print(isgeneratorfunction(c))
print(isgeneratorfunction(d))
print(isgeneratorfunction(e))
print(isgeneratorfunction(f))
print(isgeneratorfunction(g))
print(isgeneratorfunction(h))
