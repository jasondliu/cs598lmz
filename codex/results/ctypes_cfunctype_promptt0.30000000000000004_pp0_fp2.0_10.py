import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#c_int_p = ctypes.POINTER(ctypes.c_int)

#int_p = ctypes.c_int.in_dll(lib, "int_p")
#print int_p.value
#print c_int_p.from_address(int_p).contents.value

#int_pp = ctypes.c_int.in_dll(lib, "int_pp")
#print int_pp.value
#print c_int_p.from_address(int_pp).contents.value
#print c_int_p.from_address(c_int_p.from_address(int_pp).contents.value).contents.value

#int_ppp = ctypes.c_int.in_dll(lib, "int_ppp")
#print int_ppp.value
#print c_int_p.from_address(int_ppp).contents.value
#print c
