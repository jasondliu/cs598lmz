from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, {})))
print(type(FunctionType(lambda x: x, {}))())

def f():
    return f
print(type(f))
print(type(f())())

def f():
    return f()
print(type(f))
print(type(f()))

def f():
    return f
print(type(f))
print(type(f()))

def f():
    return f
print(type(f))
print(type(f()))

def f():
    return f
print(type(f))
print(type(f()))

def f():
    return f
print(type(f))
print(type(f()))

def f():
    return f
print(type(f))
print(type(f()))

def f():
    return f
print(type(f))
print(type(f()))

def f():

