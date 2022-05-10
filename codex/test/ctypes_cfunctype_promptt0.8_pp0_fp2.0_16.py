import ctypes
# Test ctypes.CFUNCTYPE()
#
# The following source code is taken from the official ctypes documentation,
# available at http://docs.python.org/library/ctypes.html
#
# Compile it with:
#
#     ctypesgen.py -lm ctypes_documentation.h -o ctypes_documentation.py
#
# You will find the generated module in the current directory.

# http://docs.python.org/library/ctypes.html
# http://docs.python.org/library/ctypes.html#ctypes.CFUNCTYPE

int    = ctypes.c_int
char_p = ctypes.c_char_p
func_p = ctypes.CFUNCTYPE(int, char_p)

