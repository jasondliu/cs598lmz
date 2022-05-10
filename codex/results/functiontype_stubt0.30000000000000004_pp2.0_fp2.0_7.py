from types import FunctionType
a = (x for x in [1])
print(type(a))

def f():
    pass

print(type(f))
print(type(FunctionType))
print(type(f) == FunctionType)

print(type(f) == type(FunctionType))

print(type(f) == type(f))

print(type(f) == type(type(f)))

print(type(type(f)) == type(type(type(f))))

print(type(type(f)) == type(type(f)))

print(type(type(f)) == type(f))

print(type(type(f)) == type(type(f)))

print(type(type(f)) == type(type(type(f))))

print(type(type(f)) == type(type(type(type(f)))))

print(type(type(type(f))) == type(type(type(type(f)))))

print(type(type(type(f))) == type(type(type(f))))

print(type(type(type(f))) == type(type(
