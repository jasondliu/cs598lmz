from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1:1}
d = '1'
e = 1
f = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(type(a) == type(b))
print(type(a) == type(c))
print(type(a) == type(d))
print(type(a) == type(e))
print(type(a) == type(f))

print(type(b) == type(c))
print(type(b) == type(d))
print(type(b) == type(e))
print(type(b) == type(f))

print(type(c) == type(d))
print(type(c) == type(e))
print(type(c) == type(f))

print(type(d) == type(e))
print(type(d) == type(f))

print(type(e) == type(f
