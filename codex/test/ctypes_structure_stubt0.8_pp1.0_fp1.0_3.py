import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong

def main():
    s = S()
    s.x = 0x123456789abcdef0
