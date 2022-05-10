import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
print X().x


class Z(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]
print Z().x
</code>
Output:
<code>0
c_int(0)
</code>
This displays the bug: the GField object is initialized to the type's default value.
However, not all code is written like this, some code goes directly to the memory exist:
<code>class Y(c_int):
    pass
print Y() # TypeError: 'ctypes.CField' object is not callable
</code>
Or, to my dismay, you cannot use a negative default as an argument. I think, this bug can be fixed by adding the following code to the ctypes.py file:
<code># Line 2857
try:
    value = type(self)()
except:
    value = self._type_
</code>

