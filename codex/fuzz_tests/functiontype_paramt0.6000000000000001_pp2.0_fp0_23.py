from types import FunctionType
list(FunctionType(add.__code__, globals(), 'add'))

add.__code__
dir(add.__code__)
add.__code__.co_argcount

add.__code__.co_varnames
add.__code__.co_argcount

def add(a, b):
    return a + b + c

add(1, 2)

add.__code__.co_varnames

add.__code__.co_argcount

def add(a, b):
    return a + b + c

add.__code__.co_argcount

def add(a, b, c):
    return a + b + c

add.__code__.co_argcount

add(1, 2)

add.__code__.co_argcount

def add(a, b, c=0):
    return a + b + c

add.__code__.co_argcount

add(1, 2)

add(1, 2, 3)

def add(a, b, c
