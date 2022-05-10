from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a), type(b))
for x in a:
    print(x)

print(type(a.__iter__))
print(type(a.__next__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

try:
    next(a)
except StopIteration:
    print('StopIteration')

print('=============================')

def f():
    yield 1

print(type(f()))
print(type(f().__iter__))
print(type(f().__next__))
print(type(f().send))
print(type(f().throw))
print(type(f().close))
for x in f():
    print(x)

print('=============================')

def g():
    yield from [1]

print(type(g()))
print(type(g().__iter__))
print(type(g().__next__))
print(type(g().send))
