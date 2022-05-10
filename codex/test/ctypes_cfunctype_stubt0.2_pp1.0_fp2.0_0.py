import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

# this is a function that takes a function as an argument
@FUNTYPE
def fun2(f):
    return f()

# this is a function that returns a function
@FUNTYPE
def fun3():
    return fun

# this is a function that returns a function that takes a function as an argument
@FUNTYPE
def fun4():
    return fun2

# this is a function that returns a function that returns a function
@FUNTYPE
def fun5():
    return fun3

# this is a function that returns a function that returns a function that takes a function as an argument
@FUNTYPE
def fun6():
    return fun4

# this is a function that returns a function that returns a function that returns a function
@FUNTYPE
def fun7():
    return fun5

# this is a function that returns a function that returns a function that returns a function that takes a function as an argument
@FUNTYPE
def fun8():
    return fun6

# this is a function that returns a function that returns a function that returns a function that returns a function
