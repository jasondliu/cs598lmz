import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"
    assert fun.__name__ == "fun"
    assert fun.__doc__ is None
    assert fun.__module__ == "test_fun"
    assert fun.__dict__ == {}
    assert fun.__defaults__ is None
    assert fun.__closure__ is None
    assert fun.__code__.co_argcount == 0
    assert fun.__code__.co_nlocals == 0
    assert fun.__code__.co_stacksize == 2
    assert fun.__code__.co_flags == 67
    assert fun.__code__.co_code == "\x64\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00"
    assert fun.__code__.co_consts == ("hello",)
    assert fun.__code__.co_names == ()
    assert fun.__code__.co_v
