from types import FunctionType
a = (x for x in [1])
print(type(a))

def f():
    for i in range(10):
        yield i

print(type(f))
print(type(f()))

def f():
    return [1, 2, 3]

print(type(f))
print(type(f()))

def f():
    return (1, 2, 3)

print(type(f))
print(type(f()))

def f():
    return {1, 2, 3}

print(type(f))
print(type(f()))

def f():
    return {'a': 1}

print(type(f))
print(type(f()))

def f():
    return 'abc'

print(type(f))
print(type(f()))

def f():
    return 1

print(type(f))
print(type(f()))

def f():
    return 1.0

print(type(f))
print(type(f()))

def f():
    return None

print
