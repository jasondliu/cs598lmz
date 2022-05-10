import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('something', ctypes.CField)]

print(type(C.something))
</code>
Output:
<code>&lt;class 'ctypes._CField'&gt;
</code>
The documentation for <code>_CField</code> is as follows:
<blockquote>
<pre><code>&lt;code&gt;class _CField(Field)
&lt;/code&gt;</code></pre>
<p>A structure/union field descriptor. This is used to describe the
  fields of a C structure or union.</p>
</blockquote>
The <code>CField</code> alias is undocumented, but it seems to be used for simplicity in many examples.

