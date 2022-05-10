import ctypes

class S(ctypes.Structure):
    x = slice(1, 2, 3)
S()
</code>
which fails with:
<code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;string&gt;", line 3, in S
TypeError: can't convert slice to ctypes type
</code>
How can I store slices in ctypes?
If this would be allowed, I believe the compiler could automatically create arrays of the right size, make slicing more efficient and so on.


A:

You'll have to do it at the C level yourself.  A <code>slice</code> is not a fixed layout object like a <code>struct</code> for example.

