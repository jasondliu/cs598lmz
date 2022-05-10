import ctypes
ctypes.cast(0, ctypes.py_object)

# /usr/include/python3.6m/pyport.h:868
def Py_CLEAR(op): # real signature unknown; restored from __doc__
    """
    Py_CLEAR(op)
    
    Clear a variable, decrementing the reference count of the object it holds.
    The variable must not be used again; it is only safe to use this macro on
    local variables.
    """
    pass

# /usr/include/python3.6m/pyport.h:878
def Py_VISIT(op): # real signature unknown; restored from __doc__
    """
    Py_VISIT(op)
    
    Visit a variable, recursively visiting all the sub-objects it holds.
    """
    pass

# /usr/include/python3.6m/pyport.h:884
def Py_SET_ERRNO(x): # real signature unknown; restored from __doc__
    """
    Py_SET_ERRNO(x)
    
    Set the platform's POS
