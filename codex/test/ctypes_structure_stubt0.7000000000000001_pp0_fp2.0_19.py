import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)

# create a S object
S_obj = S()
S_obj.x = 1
S_obj.y = 2

# get the address of the object
address = ctypes.addressof(S_obj)

# cast the address as a POINTER(S) and dereference it
S_ptr = ctypes.POINTER(S).from_address(address)
