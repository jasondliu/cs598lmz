from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

b = [x for x in [1]]
print(b)
print(type(b))
print(type(b) == GeneratorType)
print(type(b) == FunctionType)

c = {x for x in [1]}
print(c)
print(type(c))
print(type(c) == GeneratorType)
print(type(c) == FunctionType)

d = {x: x for x in [1]}
print(d)
print(type(d))
print(type(d) == GeneratorType)
print(type(d) == FunctionType)

e = [x for x in [1] if x]
print(e)
print(type(e))
print(type(e) == GeneratorType)
print(type(e) == FunctionType)

f = {x for x in [1] if x}
print(f)
print(type(f))
print(type(
