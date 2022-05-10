import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 42

print s.x
print s.x.__class__
print ctypes.c_int(42).__class__
</code>
Output:
<code>42
&lt;class '__main__.c_int'&gt;
&lt;type 'int'&gt;
</code>
I'm guessing that <code>s.x</code> is not a <code>ctypes.c_int</code> but rather a wrapper around a <code>ctypes.c_int</code>. Is there any way to get a "real" <code>ctypes.c_int</code> out of <code>s.x</code>?
Thanks!


A:

It seems that <code>ctypes.c_int</code> is a class, which is the same as <code>ctypes.c_int()</code>. However, when you do <code>s.x = 42</code>, you're assigning an integer to an instance of <code>ctypes.c_int</code>.
