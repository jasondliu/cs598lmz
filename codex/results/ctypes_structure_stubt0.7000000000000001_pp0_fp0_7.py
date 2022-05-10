import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('x', ctypes.c_int),
        ('x', ctypes.c_int),
    ]

print(S().x)
</code>
which prints 3.
This is also documented in Trac 14477:
<blockquote>
<p>Before creating the C structure, we first go through the fields and
  check if the field names are duplicated, and if so, we remove the
  duplicates. If the field name is duplicated, then the type will be
  checked to see if the field types are the same. If they are the same,
  then the type type will be used. If they are not the same, then a
  TypeError will be raised.</p>
</blockquote>
However, this doesn't work for non-platform-specific types:
<code>import ctypes

S = ctypes.c_int * 3
print(S())
</code>
This prints <code>(0, 0, 0)</code> instead of 3.
In the
