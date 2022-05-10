import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_char),
        ("c", ctypes.c_int),
    ]

s = S()
s.a = 123
s.b = 'a'
s.c = 456

print "s.a = ", s.a
print "s.b = ", s.b
print "s.c = ", s.c
print "s.x = ", s.x
</code>
Output:
<code>s.a =  123
s.b =  a
s.c =  456
s.x =  0
</code>

