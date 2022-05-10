import ctypes
# Test ctypes.CField.test_is_composite()
import ctypes._testcapi

# NULL pointer
class X(ctypes._CData):
    pass

for i in range(2):
    x = X()
    x.value = 123
    x.contents = None
    ctypes._testcapi.accept_null_ptr(x)
    if not isinstance(x.value, type(None)):
        raise TestFailed

# Non-NULL pointer
class X(ctypes._CData):
    pass

x = X()
x.value = 123
x.contents = x
ctypes._testcapi.accept_non_null_ptr(x)
if not isinstance(x.value, (int, long)):
    raise TestFailed
