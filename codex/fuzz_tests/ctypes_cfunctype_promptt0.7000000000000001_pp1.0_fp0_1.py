import ctypes
# Test ctypes.CFUNCTYPE

# Python3.7
#_cfunctype_check = ctypes.CFUNCTYPE(ctypes.c_int)
#_cfunctype_check(int) # TypeError: expected LP_c_int(), got int

# Python3.8
_cfunctype_check = ctypes.CFUNCTYPE(ctypes.c_int)
_cfunctype_check(int) # No error

# Python3.7
#_cfunctype_check(ctypes.c_int) # TypeError: expected LP_c_int(), got LP_c_int

# Python3.8
_cfunctype_check(ctypes.c_int) # No error

# Python3.7
#_cfunctype_check(ctypes.c_int(0)) # TypeError: expected LP_c_int(), got c_int instance

# Python3.8
_cfunctype_check(ctypes.c_int(0)) # No error
</code>
What's the meaning of this change?


