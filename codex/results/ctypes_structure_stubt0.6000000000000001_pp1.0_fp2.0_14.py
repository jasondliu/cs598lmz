import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()

# Note: the c_void_p.from_address() method is not very reliable in
# ctypes.  There is no guarantee that it will not raise a
# WindowsError exception, which is why we catch it and retry a few
# times.
def get_s(addr):
    for i in range(10):
        try:
            p = ctypes.c_void_p.from_address(addr)
        except WindowsError:
            time.sleep(0.1)
            continue
        return ctypes.cast(p, ctypes.POINTER(S))[0]
    raise RuntimeError('Failed to cast address %x' % addr)

def set_s(addr, s):
    for i in range(10):
        try:
            p = ctypes.c_void_p.from_address(addr)
        except WindowsError:
            time.sleep(0.1)
            continue
        ctypes.cast(p
