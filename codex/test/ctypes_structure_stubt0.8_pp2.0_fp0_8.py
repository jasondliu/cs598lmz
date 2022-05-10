import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int)]

if __name__ == "__main__":
    # This works when we initialize a new variable
    a = S()
    a.x = 1
