import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(r):
    i = ctypes.c_double.from_address(r)
    print(i.value)
    return 2*i.value    
    
callback = FUNTYPE(func)

f = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(func)
print(f(2))

#python version of example from pybind11 docs

import pybind11

@pybind11.cfunc
def cfunc(x: pybind11.ctypes.py_object):
    return f"You called cfunc with: {x}"

@pybind11.cfunc
def testbind(x: pybind11.ctypes.py_object, y: pybind11.ctypes.py_object):
    cfunc.call(x)
    return y

b = testbind.call(lambda: 1, lambda: 2)
print(b())
#this is how pybind11 gets the function pointer of a python function
x = py
