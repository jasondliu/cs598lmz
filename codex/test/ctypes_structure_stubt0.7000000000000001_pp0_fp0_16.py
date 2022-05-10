import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    def __init__(self, *args, **kwargs):
        super(S, self).__init__(*args, **kwargs)
        print(self)

print(S.__new__(S))
