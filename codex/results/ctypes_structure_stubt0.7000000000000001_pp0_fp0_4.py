import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()

lltypesystem.rffi.platform.registertype(S)

def test_rffi_platform():
    s = S()
    s.x = 42.0
    assert s.x == 42.0
    assert repr(s).startswith('<rffi.platform.S')
