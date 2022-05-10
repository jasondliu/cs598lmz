from types import FunctionType
list(FunctionType(obj()).__code__.co_varnames)

def obj():
    x = 1
    y = 2
    z = 3
    return x, y, z

print(obj())
list(obj())

def obj():
    x = 1
    y = 2
    z = 3
    return x, y, z

print(obj())

def foo():
    return 1, 2, 3

print(foo())

def foo():
    return 1, 2, 3

x, y, z = foo()

print(x)
print(y)
print(z)

foo(), 'bar'

x, y, z = foo(), 'bar'

print(x)
print(y)
print(z)

def foo():
    return 1, 2

def bar():
    return 3, 4

x, y, z, w = foo(), bar()

print(x)
print(y)
print(z)
print(w)

def foo():
    return 1, 2

def bar():
   
