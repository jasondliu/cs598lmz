import ctypes
# Test ctypes.CField

if __name__ == "__main__":

    from ctypes import *

    class foo(Structure):
        _fields_ = [("name", c_char * 10), ("age", c_short)]

    f = foo(b"hello", 33)
    f.name = b"hi"
    f.age = 34

    print(f.name, f.age)
