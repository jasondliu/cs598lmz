from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = (x for x in [1])
print(b)
print(next(b))
print(next(b))

c = [1, 2, 3, 4]
print(c)
print(next(c))

d = iter([1, 2, 3])
print(d)
print(next(d))
print(next(d))

e = iter([1, 2, 3])
print(e)
print(next(e))
print(next(e))
print(next(e))

f = iter([1, 2, 3])
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
