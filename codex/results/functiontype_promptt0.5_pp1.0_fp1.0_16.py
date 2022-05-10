import types
# Test types.FunctionType
def f():
    return 1
print type(f)
print type(f())

def f(x):
    return x
print type(f)
print type(f(1))

print type(f(1.0))

def f(x, y):
    return x + y
print type(f)
print type(f(1, 2))
print type(f(1.0, 2.0))

def f():
    return 1, 2
print type(f)
print type(f())

def f(x):
    return x, x
print type(f)
print type(f(1))
print type(f(1.0))

def f(x, y):
    return x, y
print type(f)
print type(f(1, 2))
print type(f(1.0, 2.0))

def f(x, y=1):
    return x, y
print type(f)
print type(f(1))
print type(f(1.0))

def f(x, y
