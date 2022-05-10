import ctypes

class S(ctypes.Structure):
    x = [((ctypes.c_int, ctypes.c_int), (ctypes.c_int, (ctypes.c_int,
                                                       ctypes.c_int)))]

    def __init__(self):
        self.x[0][0][0] = 0
        self.x[0][0][1] = 1
        self.x[0][1][0] = 2
        self.x[0][1][1][0] = 3
        self.x[0][1][1][1] = 4

def main():
    s = S()

    print(s.x[0][0][0])
    print(s.x[0][0][1])
    print(s.x[0][1][0])
    print(s.x[0][1][1][0])
    print(s.x[0][1][1][1])

main()
