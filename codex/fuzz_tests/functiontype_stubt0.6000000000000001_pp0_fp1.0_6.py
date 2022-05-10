from types import FunctionType
a = (x for x in [1])
b = [1]
c = []
d = {}
e = set()
f = FunctionType(lambda: None, {})

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))
print(isinstance(d, Iterator))
print(isinstance(e, Iterator))
print(isinstance(f, Iterator))
