import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16
    y = ctypes.c_uint16
    _pack_ = 1

class T(ctypes.Structure):
    x = ctypes.c_uint16
    y = ctypes.c_int8
    _pack_ = 1

a = S.from_buffer(bytearray([0x01, 0x02, 0x03, 0x04]))
b = T.from_buffer(bytearray([0x01, 0x02, 0x03, 0x04]))

