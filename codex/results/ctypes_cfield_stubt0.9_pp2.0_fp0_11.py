import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # or is it just ctypes.py_object?
type(ctypes.CField) # does it matter?

class B:
    x = 4
s = S()
print(s.x)
s.x = B.x
print(s.x)
</code>
It gives an error. The <code>s.x = B.x</code> doesn't work. But if we do something like
<code>from ctypes import (c_int, POINTER, Structure, cast)
from ctypes.test import requires

class S(Structure):
    _fields_ = [('x', c_int)]

c_int_p = POINTER(c_int)

s = S()
foo = cast(c_int_p.from_param(s), c_int_p).contents
foo.value = 5
print(s.x)
</code>
Then <code>foo.value = 5</code> successfully updates the underlying <code>s.x</code>.
My question is: Is there a way to make <code>B.x</code
