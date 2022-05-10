import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = []

s = S(x=1, y=2)
print(s.x, s.y)
</code>
<code>_fields_</code> documentation:
<blockquote>
<p>When a Structure’s <code>&lt;code&gt;_fields_&lt;/code&gt;</code> attribute is set, the class’s <code>&lt;code&gt;__slots__&lt;/code&gt;</code> attribute is set to the same names unless it is already defined, and the <code>&lt;code&gt;__dict__&lt;/code&gt;</code> and <code>&lt;code&gt;_anonymous_&lt;/code&gt;</code> attributes are deleted.</p>
</blockquote>

