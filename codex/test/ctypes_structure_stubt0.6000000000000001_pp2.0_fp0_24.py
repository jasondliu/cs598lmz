import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

inst = S()
inst.x = 1
inst.y = 2
inst.z = 3

ctypes.string_at(ctypes.addressof(inst), ctypes.sizeof(inst))

print(inst)
