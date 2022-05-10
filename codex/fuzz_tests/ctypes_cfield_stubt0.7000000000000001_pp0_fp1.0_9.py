import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Array(object):
    """
    Array(typecode [, initializer]) -> array
    Return a new array whose items are restricted by typecode, and
    initialized from the optional initializer value, which must be a list,
    string or iterable over elements of the appropriate type.
    Arrays represent basic values and behave very much like lists, except
    the type of objects stored in them is constrained. The type is specified
    at object creation time by using a type code, which is a single character.
    The following type codes are defined:
     B  signed integer 	1 	(1)
     b  signed integer 	1 	(1)
     H  unsigned integer 	2 	(2)
     h  unsigned integer 	2 	(2)
     I  unsigned integer 	4 	(4)
     i  signed integer 	4 	(4)
     Q  unsigned integer 	8 	(8)
     q  signed integer 	8 	(8)
     f  floating point 	4 	(4)
     d 
