import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class D(ctypes.Structure):
    a = ctypes.c_int
    b = ctypes.c_int

def print_struct(struct):
    print(struct.a, struct.b)

# this doesn't work
#print_struct(S)

# but this does!
print_struct(D)
