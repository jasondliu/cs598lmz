import ctypes
# Test ctypes.CFUNCTYPE

# This test is based on the following C code:
#
#   #include <stdio.h>
#   #include <stdlib.h>
#
#   typedef void (*func_ptr)(int);
#
#   void call_func(func_ptr f, int arg)
#   {
#       f(arg);
#   }
#
#   void func(int arg)
#   {
#       printf("func called with %d\n", arg);
#   }
#
#   int main(void)
#   {
#       call_func(func, 42);
#       return 0;
#   }

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype of the function we want to call
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# the function to call
def callback(arg):
    print("callback called with %d" % arg)

# convert the Python function to a C callback

