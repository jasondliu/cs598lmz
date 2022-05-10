import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

# This works...
s = S()
s.x = 1
print s.x

# But this doesn't...
p = ctypes.pointer(s)
p.contents.x = 1
print p.contents.x
</code>
The second assignment fails with a <code>ValueError</code> (invalid pointer value).
How can I assign to the variable <code>x</code> in <code>p</code>?


A:

<code>ctypes</code> objects are not really mutable.  If you want to change the value of <code>x</code> you need to assign a new value to the <code>x</code> attribute of the structure.
<code>p.contents.x = 1
</code>
is effectively a <code>del p.contents.x</code> followed by a <code>p.contents.x = 1</code>.  The first operation fails because <code>x</code> is a read-only attribute.

