from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == type(x for x in [1]))
print(type(a) is type(x for x in [1]))
print(type(x for x in [1]))

print(type(lambda x: x))
print(type(lambda x: x) is type(lambda x: x))

print(lambda x: x)
print(lambda x: x == 2)
print(lambda x: x == 2)(2)
print(lambda x: x == 2)(3)
print(lambda x: x == 2)(2) == True
print(lambda x: x == 2)(3) == True

print((lambda x: x == 2)(2))
print((lambda x: x == 2)(3))
print((lambda x: x == 2)(2) == True)
print((
