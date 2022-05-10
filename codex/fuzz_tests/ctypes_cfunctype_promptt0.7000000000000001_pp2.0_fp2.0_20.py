import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_char_p)
def bb(s):
    return s == b'q'

# Test ctypes.CFUNCTYPE with non-primitive return type
class X(ctypes.Structure):
    pass
X._fields_ = [
    ('a', ctypes.c_int)
]

@ctypes.CFUNCTYPE(X, ctypes.c_int, ctypes.c_int)
def xx(i,j):
    x = X()
    x.a = i + j
    return x

def main():
    print(bb(b'q'))
    print(bb(b'a'))
    print(xx(1,2).a)
    print(xx(2,3).a)

main()
