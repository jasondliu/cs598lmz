import ctypes

class S(ctypes.Structure):
    x = 1.0
    _fields_ = [("foo", ctypes.c_double),
                ("byte1", ctypes.c_byte),
                ("bar", ctypes.POINTER(ctypes.c_double)),
                ("byte2", ctypes.c_byte),
                ]

s = S()
s.foo = 42.0
s.bar = ctypes.pointer(ctypes.c_double(1.0))

for field_name, field_type in s._fields_:
    print("start = %r, end = %r" % (
            ctypes.addressof(getattr(s, field_name)) - ctypes.addressof(s),
            ctypes.addressof(getattr(s, field_name)) - ctypes.addressof(s) + ctypes.sizeof(field_type)))
    print(type(field_type), repr(field_type))
</code>
Output:
<code>start = 0, end = 8
&lt;class 'ctypes.c_double'&gt; c_double(
