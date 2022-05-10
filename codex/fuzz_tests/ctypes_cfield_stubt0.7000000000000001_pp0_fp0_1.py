import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

INCLUDE_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(py.path.local(__file__).strpath)),
                 'include')
]

def test_include_dirs_int():
    p = ctypes.util.find_library('m')
    if not p:
        py.test.skip("cannot find math library")
    l = ctypes.CDLL(p, include_dirs=INCLUDE_DIRS)
    assert hasattr(l, 'sin')
    assert hasattr(l, 'my_function')

def test_include_dirs_str():
    p = ctypes.util.find_library('m')
    if not p:
        py.test.skip("cannot find math library")
    l = ctypes.CDLL(p, include_dirs=INCLUDE_DIRS[0])
    assert hasattr(l, 'sin')
    assert hasattr(l, 'my_function')

def test_include_dir
