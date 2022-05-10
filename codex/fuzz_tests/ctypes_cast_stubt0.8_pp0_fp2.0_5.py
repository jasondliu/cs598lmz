import ctypes
ctypes.cast(id(foo), ctypes.py_object).value

ctypes.cast(id(foo), ctypes.py_object).value is foo

ctypes.cast(id(1), ctypes.py_object).value
 
ctypes.cast(id(None), ctypes.py_object).value

ctypes.cast(id('Hello'), ctypes.py_object).value    

import dis 
def f(x): 
    return x+1 

dis.dis(f)

import types 
def f(x): 
    return x+1 

dis.dis(types.FunctionType)

def g(x): 
    return x+1 

dis.dis(g)


def g(x): 
    print x+1 

dis.dis(g)


def g(x): 
    "Docstring"
    print x+1 

dis.dis(g)
