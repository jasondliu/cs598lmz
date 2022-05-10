import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32(0x12345678)
    y = ctypes.c_uint32(0x87654321)
    z = ctypes.c_uint32(0x7fffffff)

s = S()

for i in xrange(1000000):
    s.x ^= s.y
    s.y -= s.z
    s.z ^= s.x
    s.x += s.y
    s.y -= s.z
    s.z ^= s.x
    s.x += s.y
    s.y -= s.z
    s.z ^= s.x
    s.x += s.y
    s.y -= s.z
    s.z ^= s.x
    s.x += s.y
    s.y -= s.z
    s.z ^= s.x
    s.x += s.y
    s.y -= s.z
    s.z ^= s.x
    s.x += s.y
    s.y -= s.z
