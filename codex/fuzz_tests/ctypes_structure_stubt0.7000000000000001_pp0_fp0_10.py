import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 256

with open('/proc/cpuinfo', 'rb') as f:
    s = S.from_buffer(f)

    print s.x
</code>

