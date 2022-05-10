from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))

def fn(x):
    return x

print(type(fn))
print(type(FunctionType))

print(isinstance(fn, FunctionType))
print(isinstance(fn, type(lambda x: x)))

print(isinstance(fn, type(abs)))
print(isinstance(fn, type(int)))
print(isinstance(fn, type(str)))

print(isinstance(fn, type(a)))
print(isinstance(fn, type(b)))

print(isinstance(fn, type([])))
print(isinstance(fn, type({})))
print(isinstance(fn, type(())))

print(isinstance(fn, type(None)))
print(isinstance(fn, type(Ellipsis)))
print(isinstance(fn, type(NotImplemented)))

print(isinstance(fn, type(...)))

print(isinstance(fn, type(1)))
print(isinstance(fn, type(1.0)))
