from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

a = (x for x in [1])
print(next(a))
print(next(a))

a = (x for x in [1])
print(type(a))
print(a)
print(isinstance(a,FunctionType))

def g():
    yield 1

a = g()
print(type(a))
print(a)
print(isinstance(a,FunctionType))

print(isinstance(g,FunctionType))

print(next(a))
print(next(a))

def f():
    return 1

a = f()
print(type(a))
print(a)
print(isinstance(a,FunctionType))

print(isinstance(f,FunctionType))

print(next(a))
print(next(a))

# int, str, bool 等类型都是可迭代对象，但是不是迭代器

a = 1
print(
