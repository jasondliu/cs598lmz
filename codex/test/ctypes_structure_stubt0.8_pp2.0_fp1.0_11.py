import ctypes

class S(ctypes.Structure):
    x = 0
    _fields_ = [
        ('p', ctypes.c_void_p),
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ]

def main():
    s = S()
