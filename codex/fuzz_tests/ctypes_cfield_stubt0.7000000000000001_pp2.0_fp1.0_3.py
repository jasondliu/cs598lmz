import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_interp_w_cfield():
    S_x = S.x
    import gc
    # this raised an unexpected AttributeError once
    # (weirdly, it didn't happen every time)
    return [gc.get_referents(S_x)]

print(test_interp_w_cfield())
