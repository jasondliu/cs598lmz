import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def main():
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    buf = ctypes.create_string_buffer(s, 3*s.x.size)

    print(buf.raw)
