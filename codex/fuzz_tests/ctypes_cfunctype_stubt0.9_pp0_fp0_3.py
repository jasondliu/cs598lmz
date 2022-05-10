import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'Hello, world!'

with GIL():
    pass

assert fun.__python_function__() == 'Hello, world!'

with GIL():
    assert fun() == 'Hello, world!'

# GIL() as a function.  The function itself MUST NOT be a GILFunction,
# because it cannot be called without arguments.  CPython's
# PyCFunction_Call() takes care of this, and provides the type checking.
# cppyy's cppyy.gbl.gInterpreter.ProcessLine() does NOT take care of
# this.  So test this functionality by passing the function a lambda
# call, which should NOT work if type checking is not done.
GIL(fun)(lambda: 42) # should raise an exception
