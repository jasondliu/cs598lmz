import ctypes
# Test ctypes.CFUNCTYPE

libc = CDLL(ctypes.util.find_library("c"))

def test(restype, argtypes, *args):
    func = CFUNCTYPE(restype, *argtypes)(("test_func", libc))
    res = func(*args)
    print(res)
    if restype in (c_int, c_long, c_longlong):
        assert res == sum(args)

for restype in [c_int, c_long, c_longlong]:

    test(restype, [restype], 1)
    test(restype, [restype], 42)
    test(restype, [restype], -42)
    test(restype, [restype], 0xffff)

    test(restype, [restype, restype], 1, 1)
    test(restype, [restype, restype], 1, 2)
    test(restype, [restype, restype], 2, 1)
    test(restype, [restype, restype], 0xffff, 1)
    test(rest
