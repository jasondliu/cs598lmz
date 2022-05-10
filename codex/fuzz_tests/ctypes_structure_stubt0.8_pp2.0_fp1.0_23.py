import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.0)
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("next", ctypes.POINTER(ctypes.c_double))
    ]

s = S()
s.y = 1.0
s.next = ctypes.byref(s.x)
print(s.x)
print(s.y)
print(s.next[0])
print('x' in s._fields_)
print(hasattr(s,'x'))
</code>
For the record, I'd prefer using a class with properties, but this is what I'm stuck with.


A:

By and large, no.  You can modify the <code>_fields_</code> tuple/list to add new items (or remove existing ones), but that's about it.  You can't "upgrade" the <code>ctypes</code> type assigned to an existing entry from a simple type like <code>c_int</code> to a complex type like <code>St
