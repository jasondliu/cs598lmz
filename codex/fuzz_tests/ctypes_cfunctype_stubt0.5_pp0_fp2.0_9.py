import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_py_callable():
    assert isinstance(fun, ctypes.PyCallable)
    assert isinstance(fun, ctypes.CFUNCTYPE)

@pytest.mark.skipif(sys.platform == "win32", reason="win32 not supported")
def test_signal():
    import signal
    import ctypes
    import ctypes.util
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    def handler(signum, frame):
        pass

    signal.signal(signal.SIGUSR1, handler)
    old = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(libc.signal(signal.SIGUSR1, 0))
    libc.signal(signal.SIGUSR1, old)

def test_callback_in_del():
    import ctypes
    import gc
    lib = ctypes.CDLL(ctypes.util.find_library("c"))
    class
