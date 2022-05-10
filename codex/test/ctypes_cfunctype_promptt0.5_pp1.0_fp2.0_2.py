import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE, which is used to create function pointers.
# The function pointers may be passed to C functions which expect a function
# pointer as an argument.

# The following C code should be compiled as a dynamic library, and loaded
# by ctypes.

# The code uses the Python/C API to call back into Python.

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

#ifndef _WIN32
#define DLLEXPORT
#else
#define DLLEXPORT __declspec(dllexport)
#endif

