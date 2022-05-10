import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(42)

    _fields_ = [('y', ctypes.c_void_p)]

def test(impl, loop):
    obj = impl.IntObject(5)
    assert obj.value == 5
    assert obj.value == obj.value

    obj.value = 6
    assert obj.value == 6
    assert obj.value == obj.value

    # S is a structure and it has __len__()
    obj = impl.new1(S(), impl.PyLifetime.PY_REF_ONLY)
    assert obj.chkrefcount(0)

    obj2 = impl.new1(S(), impl.PyLifetime.PY_REF_STORAGE, 2)
    assert obj2.chkrefcount(2)

    # The second argument to call_method2 should be a PyObject*
    o = impl.PyObject()
    assert obj2.call_method2(1, o, 2).value == 3
    assert obj2.call_method2(1, o, 2).value == \
        obj
