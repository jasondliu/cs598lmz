import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

assert fun() == "hello"

# Test that we can pass a function as an argument
@FUNTYPE
def fun2(f):
    return f()

assert fun2(fun) == "hello"

# Test that we can return a function
@FUNTYPE
def fun3():
    @FUNTYPE
    def fun4():
        return "hello"
    return fun4

assert fun3()() == "hello"

# Test that we can pass a function as an argument, and return a function
@FUNTYPE
def fun5(f):
    @FUNTYPE
    def fun6():
        return f()
    return fun6

assert fun5(fun)() == "hello"

# Test that we can pass a function as an argument, and return a function
@FUNTYPE
def fun7(f):
    @FUNTYPE
    def fun8():
        return f()
    return fun8

assert fun7(fun)() == "hello"

# Test that we can pass a function as an argument, and return a function
@FUNTYPE
