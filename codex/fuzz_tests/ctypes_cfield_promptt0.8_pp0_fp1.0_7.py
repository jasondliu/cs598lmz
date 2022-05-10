import ctypes
# Test ctypes.CField

has_type = ctypes.create_string_buffer('ABCDEFGH')
no_type = 'ABCDEFGH'

class test_type(ctypes.Structure):
    _fields_ = [('a', ctypes.CField)]

test = test_type()

test.a = has_type
test.a = no_type

try:
    expect_error = False
    test.a = None
except ValueError:
    expect_error = True

assert expect_error

try:
    expect_error = False
    test.a = 5
except ValueError:
    expect_error = True

assert expect_error
