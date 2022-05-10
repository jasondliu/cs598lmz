import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte


class S2(ctypes.Structure):
    x = ctypes.c_longlong


class S3(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte
    z = ctypes.c_byte
    w = ctypes.c_byte


def check(S, v):
    x = S()
    x.x = v
    assert x.x == v
    return x.x, x.y


def test_alignment():
    assert ctypes.alignment(S) == 1
    assert ctypes.alignment(S2) == 8
    assert ctypes.alignment(S3) == 1
    assert ctypes.sizeof(S) == 2
    assert ctypes.sizeof(S2) == 8
    assert ctypes.sizeof(S3) == 4
    assert check(S, 1) == (1, 0)
    assert check(S, 255) == (255, 0)
    assert check
