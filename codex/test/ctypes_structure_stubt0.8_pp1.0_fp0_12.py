import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

    def __init__(self):
    # Just for sure calling the default constructor does not change anything
        print("x1", self.x)
        super(S, self).__init__()
        print("x2", self.x)

s = S()
print("x3", s.x)
