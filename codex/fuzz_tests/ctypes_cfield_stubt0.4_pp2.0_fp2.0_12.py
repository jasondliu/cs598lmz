import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self._fields_ = [('x', ctypes.c_int)]
        self._bases_ = (S,)

print C.__bases__
print C.__mro__
print C().__class__
print C().x
</code>
Output:
<code>(&lt;class '__main__.S'&gt;,)
(&lt;class '__main__.C'&gt;, &lt;class '__main__.S'&gt;, &lt;type 'object'&gt;)
&lt;class '__main__.C'&gt;
0
</code>

