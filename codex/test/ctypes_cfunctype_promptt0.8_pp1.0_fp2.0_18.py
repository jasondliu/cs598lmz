import ctypes
# Test ctypes.CFUNCTYPE()
# To support multi-threading, #include "pthread.h" in cg_test.c
# and include necessary pthread libraries when linking (e.g. -lpthread)
#
# Declare a ctypes pointer to f1()
