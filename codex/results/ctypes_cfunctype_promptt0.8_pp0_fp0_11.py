import ctypes
# Test ctypes.CFUNCTYPE...

# Callback type prototypes
CB_C_IntVoid = ctypes.CFUNCTYPE(ctypes.c_int)
CB_C_IntInt = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CB_C_IntIntPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double))

# Callback functions
@CB_C_IntVoid
def cb_c_intint_void(i):
    print ("cb_c_intint_void", i)
    return i+1

@CB_C_IntInt
def cb_c_intint_int(i):
    print ("cb_c_intint_int", i)
    return i*2

@CB_C_IntIntPtr
def cb_c_intintptr_intptr(i, val):
    print ("cb_c_intintptr_intptr", i, val[0])
    return
