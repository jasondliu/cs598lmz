import ctypes
# Test ctypes.CFields, some of the constructors don't work with
# CFields, so we use from_address() instead
ctypes.c_int.in_dll(ctypes, '__ob_refcnt')
# We don't have a C++ compiler, so pybind11 is out of the question.
