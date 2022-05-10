import ctypes

class S(ctypes.Structure):
    x = 6

    _fields_ = [("str2", "|B"), ("str1", "|b")]

    _anonymous_ = ["str1", "str2"]

print(S().str1)
</code>
Outputs:
<code>0
</code>
However, in Python 2, the b'original' value of the <code>char</code> is:
<code>'\x00'
</code>


A:

From Python 2.6 to 2.7, ctypes added support for object-like structs (via <code>_asobject_</code>), which allows you to set/get attributes from a struct as if it were a standard object. This gives you a nice way to abstract the access to a struct, as this code shows:
<code>#!/usr/bin/python
import ctypes

class S(ctypes.Structure):
    _fields_ = [("str1", "|b")]

s = S()
s.str1 = 4
print "str1:", s.str1
</code>
Output:
<
