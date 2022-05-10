import ctypes

class S(ctypes.Structure):
    x = ()
    y = ''

struct1 = S()
struct2 = S()

# Strictly speaking, the following line is not required, but it increases
# chances to reproduce the bug in case this file is run as a standalone
# program by making struct2 and struct1 share the same instance of
# the empty tuple.
struct2.x = struct1.x

# Add an element to struct1.x.
struct1.x += (1,)

