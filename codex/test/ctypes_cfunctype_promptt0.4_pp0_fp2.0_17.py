import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is only run if ctypes is compiled with the
# macro Py_USING_UNICODE.
#
# The test passes if the output is:
#
#   ord(u'a') = 97
#   ord(u'b') = 98
#   ord(u'c') = 99
#
# Otherwise the test fails.

if ctypes.sizeof(ctypes.c_wchar) != 2:
    raise SystemExit

if not hasattr(ctypes, "Py_UNICODE"):
    raise SystemExit

Py_UNICODE = ctypes.Py_UNICODE

@ctypes.CFUNCTYPE(None, Py_UNICODE)
def func(c):
    print("ord(u'%c') = %d" % (c, ord(c)))

func(u'a')
func(u'b')
func(u'c')
