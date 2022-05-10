import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

libfoo = ctypes.CDLL(find_library("foo"))

foo = libfoo.foo
foo.argtypes = [ctypes.CField]
foo.restype = ctypes.c_int

foo(S.x)

a = ctypes.c_int()
foo(a)
</code>
or
<code>foo.argtypes = [ctypes.c_int]
</code>
... in case the field fits int the address (or double).
CType size
In case neither works, you need to look at the size of the CType the field is defined for.
<code>S = ctypes.c_char * 16

libfoo = ctypes.CDLL(find_library("foo"))

foo = libfoo.foo
foo.argtypes = [type(S.__getitem__(0))]
foo.restype = ctypes.c_int

foo(S.__getitem__(0))

a = ctypes.c_char()
foo(a)
</code>
or
<code>foo.argtypes
