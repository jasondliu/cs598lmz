import ctypes
# Test ctypes.CFUNCTYPE()
def OCICharbuffer(n):
    kname = 'ub1'
    a = (-ctypes.c_int * n)()
    kname = kname + '*'
    func_char = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), klen)
    func_switch = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), klen)
    b = ctypes.c_int(ctypes.addressof(a))
    c = ctypes.pointer(ctypes.c_int(ctypes.addressof(a)))
    v = OCICharbuffer(n)
    vf = OCICharbuffer(n)
    h = n
    # Make call
    print(func_char(h, c, klen))
    # Verify address
    print(ctypes.addressof(a) == ctypes.addressof(a
