import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p()

def main():
    c = S()
