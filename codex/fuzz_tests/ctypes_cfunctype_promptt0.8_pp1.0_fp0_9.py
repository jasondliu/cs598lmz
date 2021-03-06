import ctypes
# Test ctypes.CFUNCTYPE(...)

# Compile with:
#     gcc -o test_cfunctype -O2 test_cfunctype.c
# or:
#     gcc -o test_cfunctype -Og -g test_cfunctype.c
#
# Run with:
#     ./test_cfunctype
#
# Look at the output of:
#     gdb ./test_cfunctype
#
# The point of this test is to ensure that the C code for a function
# generated by ctypes.CFUNCTYPE() does not contain any references to
# the original Python function object which contains the compiled
# code.  Without this, it would be hard to avoid memory leaks: when
# the original function object goes away, its code would still be
# referenced by the C function object, even though the Python object's
# destructor has already run, so the reference count on the code would
# never go to zero.
#
# On Windows the C code is compiled to a DLL and loaded dynamically;
# the point of this test is to ensure that the DLL is closed when
