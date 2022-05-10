import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def callback(data):
    print("callback: " + bytes(data).decode("utf-8"))
    return 0

def test_callback():
    cb = FUNTYPE(callback)
    t = ctypes.c_char_p(b"Hello")
    assert cb(t) == 0

if __name__ == "__main__":
    test_callback()
