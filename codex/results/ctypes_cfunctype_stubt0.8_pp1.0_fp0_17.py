import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'spam'
fun()
 
# Function pointer as argument
def bar(fun):
    return fun()
bar(fun)
# But see later for a better way!

# Passing arguments to callback
@FUNTYPE
def fun(x):
    return x
fun(10)

@FUNTYPE
def fun(s):
    return 3*s
fun('spam')

# Passing more than one argument
@FUNTYPE
def fun(s1, s2):
    return s1 + ' ' + s2
fun('spam', 'and eggs')

# CFUNCTYPE can't parse more than one argument
# (AttributeError: CFUNCTYPE argument 1 must be type, not tuple)
# FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, (ctypes.py_object, ctypes.py_object))
# @FUNTYPE
# def fun(s1, s2):
#     return s1 + ' ' + s2
# fun('spam', 'and eggs')

# Use FUNTYPE2 instead, but
