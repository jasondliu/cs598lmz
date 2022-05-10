import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64()
    y = ctypes.c_int64()

So I have a C function, which prints the values of a struct:

void print_struct(struct struct_s *s) {
    printf("%lld %lld\n", s->x, s->y);
}

Now I want to call this from Python, using ctypes. I tried this:

#!/usr/bin/python3
import ctypes

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int64),
                ("y", ctypes.c_int64)]

lib = ctypes.CDLL("libfoo.so")

s = S(9, 4)
lib.print_struct.argtypes = [ctypes.POINTER(S)]
lib.print_struct.restype = ctypes.c_void_p
print("BEFORE:", s.x, s.y)
lib.print_struct(s);
print("AFTER:", s.x, s.y)

This works
