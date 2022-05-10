import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    y = ctypes.c_uint32()
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test(S):
    print('S.x: ', S.x)
    print('S.y: ', S.y)

s = S(1, 2)
test(S)
