import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

ctypes.pointer(s)
</code>
But this doesn't work:
<code>&gt;&gt;&gt; s.__ctypes_from_outparam__()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'S' object has no attribute '__ctypes_from_outparam__'
</code>
Why is this? Is there another way to get a pointer to a <code>ctypes.Structure</code> from the <code>ctypes</code> module?


A:

I don't know where your <code>__ctypes_from_outparam__</code> function is coming from.  It's not part of the standard <code>ctypes</code> module.
You can get a pointer to a <code>Structure</code> instance by creating a new pointer:
<code>p
