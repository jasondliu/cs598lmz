import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint32)


class ProxyDriver(Function):

    def __init__(self, ffi):
        self.ffi = ffi
        self.closed = False

    def _call(self, N):
        return self.func(N, 1)

    def close(self):
        self.closed = True
        self.func = None


@tree_to_obj_test_helper
def test_simple(driver, lib, args):
    assert lib.my_add(5, 6) == 11


def test_argtypes(driver, lib, args):
    lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.add.restype = ctypes.c_int
    assert lib.add(5, 6) == 11


def test_convert(driver, lib, args):
    lib.my_add.argtypes = [float, float]
    lib.my_add.restype = float
    assert lib.my_add(4.4, 5.5) == 9.9
