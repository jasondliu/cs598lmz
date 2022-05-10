import ctypes
# Test ctypes.CFUNCTYPE
# ctypes.CFUNCTYPE(resulttype, *argtypes, use_errno=False, use_last_error=False)

# int (*func)(int, double)
# int (*func)(int, int)
# int (*func)(int, int)

# If a function is declared with a variable number of arguments
# (using ... in the declaration), the array should contain a single
# item: None.

# The use_errno and use_last_error keyword arguments are only used by
# Windows COM functions.

# http://stackoverflow.com/questions/3629007/ctypes-and-callback-functions

# --------------------------
# int (*func)(int, double)
# --------------------------

# int (*func)(int, double)

# int (*func)(int, int)

# int (*func)(int, int)

# If a function is declared with a variable number of arguments
# (using ... in the declaration), the array should contain a single
# item: None.

# The use_errno and use_last_error
