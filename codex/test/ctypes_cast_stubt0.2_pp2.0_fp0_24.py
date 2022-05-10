import ctypes
ctypes.cast(0, ctypes.py_object)

# /usr/include/python3.6m/pyport.h:852
def Py_CLEAR(op): # real signature unknown; restored from __doc__
    """
    Py_CLEAR(op)
    
    Clear a variable, e.g. Py_CLEAR(op) is equivalent to op = NULL.
    """
    pass

# /usr/include/python3.6m/pyport.h:853
def Py_SETREF(op, op2): # real signature unknown; restored from __doc__
    """
    Py_SETREF(op, op2)
    
    Set a variable to a new value, e.g. Py_SETREF(op, op2) is equivalent to op = op2.
    """
    pass

# /usr/include/python3.6m/pyport.h:854
