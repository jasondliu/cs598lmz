import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64

s = S()
print(ctypes.sizeof(s))
print(s.x)
</code>


A:

The documentation says, in part:
<blockquote>
<p>This [module] provides C compatible data types, and allows calling functions in DLLs or shared libraries.</p>
</blockquote>
The documentation also states that the <code>uint64</code> type is a synonym for <code>c_uint64</code> and that it is defined as:
<blockquote>
<pre><code>&lt;code&gt;class c_uint64(_SimpleCData):
    """c_uint64(value) -&amp;gt; unsigned integer 64 bit value
    This is the C unsigned int type, which is a 64 bit integral value. Participates in numeric operations, including comparisons."""
    _type_ = "Q"
    __ctype_le__ = _ctype_le
    __ctype_be__ = _ctype_be
&lt;/code&gt;</code></pre>
</block
