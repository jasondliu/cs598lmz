import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it should be callable
# and have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(42)

# This is a function pointer type, it should be callable
# and have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(42)

# This is a function pointer type, it should be callable
# and have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(42)

# This is a function pointer type, it should be callable
# and have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(42)

# This is a function pointer type, it should be callable

