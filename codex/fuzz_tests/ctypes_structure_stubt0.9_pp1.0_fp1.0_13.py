import ctypes

class S(ctypes.Structure):
    x = ctypes.wintypes.DWORD

s = S()
s.x
</code>
Output:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'S' object has no attribute 'x'
</code>
To make it work, you need to initialize the object by calling
<code>ctypes.Structure.__init__(s)
</code>
This is exactly what the <code>_fields_</code> is doing when Python calls <code>__init__</code>. Whenever you create a <code>Structure</code> subclass with <code>_fields_</code> defined, Python calls <code>__init__</code> with the keyword argument <code>_fields_</code> (this is what is going on in <code>class S(ctypes.Structure): x = ctypes.wintypes.DWORD</code>). Otherwise <code>__init__</code> is not  called.

