from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
print(a)
print(b)
print(c)

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(a.__name__)
print(b.__name__)
print(c.__name__)

print(a.__closure__)
print(b.__closure__)
print(c.__closure__)

print(a.__closure__[0].cell_contents)
print(b.__closure__[0].cell_contents)
print(c.__closure__[0].cell_contents)

print(a.__closure__[0].cell_contents.__closure__)
print(b.__closure__[0].cell_contents.__closure__)
print(c.__closure__[0].cell_contents.__closure__)

print(a.__closure__[0].cell_contents.__
