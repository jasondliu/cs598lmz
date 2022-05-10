import ctypes
# Test ctypes.CFUNCTYPE()
# To support multi-threading, #include "pthread.h" in cg_test.c
# and include necessary pthread libraries when linking (e.g. -lpthread)
#
# Declare a ctypes pointer to f1()
f1 = ctypes.CDLL('./libcg_test.so').f1
f1_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
f1_ptr = f1_c(f1)
#
# Input data for the function
f1_in = (ctypes.c_int * 1)()
f1_in[0] = 4
#
# Output data from the function
f1_out = (ctypes.c_int * 1)()
#
# Call the function
f1_ptr(f1_in, f1_out)
#
# Print the output array
print("f1_out is {}".format(f1_out[0]))
#
# Determine the return value of the call

