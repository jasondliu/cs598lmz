import ctypes

class S(ctypes.Structure):
    x = ((1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,))
    _fields_ = [
        ('b', ctypes.c_byte, 3),
        ('pad', ctypes.c_byte, 5),
    ]

