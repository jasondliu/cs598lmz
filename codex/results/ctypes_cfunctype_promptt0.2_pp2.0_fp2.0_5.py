import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX On Win64, the calling convention is ignored, and cdecl is always used.
# This is a bug in ctypes.

# cdecl
cdecl_call = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("cdecl_call", lib), ((1,),))
assert cdecl_call(2) == 2

# stdcall
stdcall_call = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("stdcall_call", lib), ((2,),))
assert stdcall_call(2) == 2

# fastcall
fastcall_call = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("fastcall_call", lib), ((3,),))
assert fastcall_call(2) == 2

# This should fail with a TypeError
try:
    ctypes.CFUNCTYPE
