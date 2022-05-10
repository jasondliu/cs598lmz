import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# test c_char_p.from_param
def test(val):
    print("testing %s"%val)
    f = ctypes.CField("x", ctypes.c_char_p).from_param
    val = f(val)
    print(ctypes.addressof(val))
    print(val.value)
    return S(val)

s = test("Hello World")
print(s.x)


# Issue #9467: a char format specifier should not be used in
# Py_BEGIN_ALLOW_THREADS / Py_END_ALLOW_THREADS
#
# libffi doesn't declare any of its functions in THREAD_SAFE mode when
# building with Visual Studio, so let's not try to run this test then.
if hasattr(ctypes.CDLL(None), "Py_BEGIN_ALLOW_THREADS"):
    import _ctypes_test
    import _testcapi
    for i in range(10000):
        value = _ctypes_test.lib.threadlock_ac
