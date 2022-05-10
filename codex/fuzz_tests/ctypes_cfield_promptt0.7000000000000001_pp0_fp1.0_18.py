import ctypes
# Test ctypes.CField
def test_CField_1():
    class MyStruct(ctypes.Structure):
        _fields_ = [("test", ctypes.c_char_p)]

    s = MyStruct()
    s.test = "abc"
    assert s.test == "abc"


def test_CField_2():
    class MyStruct(ctypes.Structure):
        _fields_ = [("test", ctypes.c_char_p)]

        def __del__(self):
            print("del")

    s = MyStruct()
    s.test = "abc"
    del s

# Test ctypes.c_buffer
def test_c_buffer_1():
    s = ctypes.c_buffer(b"abc")
    assert s[:] == b"abc"
    s[:] = b"def"
    assert s[:] == b"def"

def test_c_buffer_2():
    s = ctypes.c_buffer("abc")
    assert s[:] == b"abc"
    s[:] = "def"
    assert
