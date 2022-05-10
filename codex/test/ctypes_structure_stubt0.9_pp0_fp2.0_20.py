import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = 16 * "ab"
    z = 16 * "cd"
    w = 16 * "ef"

strct = S()

strct.x = 123
strct.y = "hello"

buf = ctypes.create_string_buffer(16)
