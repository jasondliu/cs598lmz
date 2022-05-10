import ctypes

class S(ctypes.Structure):
    x = b'\x01\x02\x03\x04'
    y = b'\x05\x06\x07\x08'

s = S()

print(s.x)
print(s.y)
