import ctypes
# Test ctypes.CField
import _ctypes_test

def test(value, type_):
    ct_value = ctypes.c_short.from_address(
        ctypes.addressof(_ctypes_test.short_value))
    ct_value.value = value
    assert type_(ct_value.value) is ct_value.value

test(1, int)
test(1.0, float)
test(1+2j, complex)
test('abc', str)
test(b'abc', bytes)
test(b'abc'.decode('ascii'), str)
test(u'abc', str)
test(u'abc'.encode('ascii'), bytes)
