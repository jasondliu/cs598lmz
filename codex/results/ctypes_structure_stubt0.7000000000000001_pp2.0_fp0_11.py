import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

d = S()
s = struct.Struct("&lt;d&gt;&lt;d&gt;&lt;d&gt;")
a = array.array("d", [1,2,3])

s.pack_into(a, 0, d)

print(a)
</code>
I get this error:
<code>struct.error: cannot convert argument to double
</code>
How can I unpack the structure into the array?


A:

The <code>&lt;d</code> format specifier is for padding, not for unpacking.
This works:
<code>#!/usr/bin/env python

import struct
import ctypes

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

d = S()
s = struct.Struct("&
