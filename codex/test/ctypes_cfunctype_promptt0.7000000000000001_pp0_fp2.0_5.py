import ctypes
# Test ctypes.CFUNCTYPE.
#
# ctypes.CFUNCTYPE(return_type, *parameter_types)
#
# return_type -- The result type of the function. This must be a ctypes type.
# parameter_types -- A sequence specifying the types of parameters expected by the function. Each item in the sequence must be a ctypes type.
#
#
# Create a new function type with an argument type of c_int and a return type of c_int.
#
# >>> CFUNCTYPE(c_int, c_int)
# <class 'ctypes.CFUNCTYPE'>
# >>> CFUNCTYPE(c_int, c_int)()
# <ctypes.CFUNCTYPE object at 0x7fddf49dbc30>
# >>> CFUNCTYPE(c_int, c_int)(lambda x: x)
# <ctypes.CFUNCTYPE object at 0x7fddf49dbbe0>
# >>> CFUNCTYPE(c_int, c_int)(lambda x: x).__call__(2)

