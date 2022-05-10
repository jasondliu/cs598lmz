import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit different from the others.  It is a test of the
# ctypes module itself.  It tests the CFUNCTYPE function, which is
# used to create C callbacks.
#
# The test is a bit tricky because it uses the "ctypes" module to
# create a C callback, which is then called from C code.  The C
# callback uses the "ctypes" module to call a Python function.  This
# means that the "ctypes" module must be fully initialized before the
# C code is called, but the C code cannot call the Python callback
# until the "ctypes" module is initialized.
#
# To handle this, the test is implemented in two parts.  The first
# part is implemented in pure Python.  It uses ctypes to create a C
# callback, and then calls a C function to call the callback.  The C
# callback uses ctypes to call a Python function.  The Python
# function records the value passed from the C code, and returns a
# value to the C code.  The C code records the value returned from
# the
