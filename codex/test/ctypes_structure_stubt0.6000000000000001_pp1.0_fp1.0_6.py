import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class P(ctypes.Structure):
    _fields_ = [('b', ctypes.c_byte), ('a', ctypes.c_char_p)]

def main():
    s = S()
