import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_is_descriptor():
    assert isinstance(S.x, ctypes.CField)
    assert isinstance(S().x, ctypes.CField)

def test_cfield_set(tmpdir):
    import sys
    import os
    import gc

    fn = str(tmpdir) + "/cfield_set.so"

    with open(fn, "wb") as f:
        f.write(b"\x03\x00\x00\x00" * 64 * 1024)

    mm = ctypes.pythonapi.PyMem_Malloc
    mm.restype = ctypes.c_void_p
    mm.argstype = ctypes.c_size_t
    mv = ctypes.pythonapi.PyMem_WriteUcs4
    mv.restype = ctypes.c_size_t
    fp = os.open(fn, os.O_RDWR)
    ctypes.pythonapi.PyFile_SetBufSize(fp, 0)
    f = os.fdopen
