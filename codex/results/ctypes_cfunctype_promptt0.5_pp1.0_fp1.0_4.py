import ctypes
# Test ctypes.CFUNCTYPE()

# ctypes.CFUNCTYPE()
# Create a C callable function from a Python callable object.
#
# The flags argument can be a bitwise ORed combination of:
#
# FUNCFLAG_CDECL
# FUNCFLAG_PYTHONAPI
# FUNCFLAG_USE_ERRNO
# FUNCFLAG_USE_LASTERROR
#
# The default is FUNCFLAG_CDECL.

# FUNCFLAG_CDECL
# The Python callable is converted to a C function that uses the
# standard C calling convention.

# FUNCFLAG_PYTHONAPI
# The Python callable is converted to a C function that uses the
# standard Python C API calling convention.

# FUNCFLAG_USE_ERRNO
# The Python callable is converted to a C function that uses the
# standard C calling convention and sets the external variable errno
# if the function raises an exception.

# FUNCFLAG_USE_LASTERROR
# The Python callable is converted to a C function that uses the
# standard C calling
