import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()
    y = ctypes.c_double()
    z = ctypes.c_double()

ctypes.pythonapi.PyBuffer_FromReadWriteMemory.restype = ctypes.py_object
ctypes.pythonapi.PyBuffer_FromReadWriteMemory.argtypes = (
    ctypes.c_void_p,
    ctypes.c_longlong,
)

s = S()
buf = ctypes.pythonapi.PyBuffer_FromReadWriteMemory(
    ctypes.addressof(s),
    ctypes.sizeof(s),
)
print(repr(buf.tobytes()))

s.x = 0.2
s.y = 0.3

buf.get_address()[ctypes.sizeof(s.x)::] = 0

# prints <Buffer ...>
# prints b'\x00\x00\x00\x00\x00\x00\x00\x00'
# prints b'\xcd\xcc\x4c\x3f\x00
