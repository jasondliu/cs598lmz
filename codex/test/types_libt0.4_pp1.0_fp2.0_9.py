import types
types.FunctionType

def outer():
    def inner():
        print('inner')
    return inner

f = outer()
f()

def outer():
    x = 1
    def inner():
        x = 2
        print(x)
    inner()
    print(x)

outer()

def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print(x)
    inner()
    print(x)

outer()

def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
add_5(3)

def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print(x)
    return inner

f = outer()
f()

def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
add_5(3)

