import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()
    foo = ctypes.c_char_p()

s = S()
s.x = 1.0
s.y = 0.0
s.z = 0.0
s.foo = 'bar'
print s.foo
</code>
This prints "bar". However, if I try to access <code>s.foo</code> through a pointer:
<code>from ctypes import *

class S(Structure):
    x = c_double()
    y = c_double()
    z = c_double()
    foo = c_char_p()

s = S()
s.x = 1.0
s.y = 0.0
s.z = 0.0
s.foo = 'bar'

p = POINTER(S)()
p = pointer(s)
print p.contents.foo
</code>
I get a segmentation fault:
<code>python test.py

Program received signal SIG
