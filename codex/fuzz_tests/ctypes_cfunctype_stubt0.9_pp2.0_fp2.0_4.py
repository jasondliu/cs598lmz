import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 'hi'

s = ctypes.string_at(FUNTYPE(fun)())
print s

assert s == 'hi'


# test ctypes.string_at on unicode
s = ctypes.string_at(u'foo')
print s
assert s == 'foo'
s = ctypes.string_at(u'f\xf3\xf3')
print s
assert s == 'f\xf3\xf3'


# test ctypes.wstring_at
s = ctypes.wstring_at(u'bar')
print s
assert s == u'bar'
s = ctypes.wstring_at(u'f\xf3\xf3')
print s
assert s == u'f\xf3\xf3'

print ('destination buffer overrun' in ctypes.string_at.__doc__)


# issue 71: get_errno propagation through ctypes
OSErr = ctypes.c_int
if os.name != 'nt':  # test doesn't make much sense on Windows
    libc = ctypes.CD
