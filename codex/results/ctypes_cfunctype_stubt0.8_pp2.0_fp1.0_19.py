import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
ITER_OBJECT = FUNTYPE
class array(object):
    """
    array(typecode [, initializer]) --> array
    
    Return a new array whose items are restricted by typecode, and
    initialized from the optional initializer value, which must be a list,
    string or iterable over elements of the appropriate type.
    
    Arrays represent basic values and behave very much like lists, except
    the type of objects stored in them is constrained. The type is specified
    at object creation time by using a type code, which is a single character.
    The following type codes are defined:
    
    Type code   C Type             Minimum size in bytes 
    'c'         character           1 
    'b'         signed integer      1 
    'B'         unsigned integer    1 
    'u'         Unicode character   2 (see note) 
    'h'         signed integer      2 
    'H'         unsigned integer    2 
    'i'         signed integer      2 
    'I'         unsigned integer    2 
    'l'         signed integer     
