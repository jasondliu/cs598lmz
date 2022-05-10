from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

def f():
    print('hello')

print(type(f))
print(type(f) == FunctionType)
print(type(f) == type(lambda x: x))

def f():
    print('hello')

print(type(f))
print(type(f) == FunctionType)
print(type(f) == type(lambda x: x))
