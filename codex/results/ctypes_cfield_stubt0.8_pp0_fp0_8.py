import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField._length_ = S._fields_[0][1]._length_

class SP(ctypes.Structure):
    pass
SP._fields_ = [('p', ctypes.POINTER(S))]

s = S(10)

sp = SP(s)
print(sp.p.contents.x)
</code>
<blockquote>
<p>10</p>
</blockquote>
But, you'd better use:
<code>sp = SP(ctypes.pointer(s))
</code>
<blockquote>
<p>10</p>
</blockquote>
Or:
<code>sp = SP()
sp.p = ctypes.pointer(s)
</code>
<blockquote>
<p>10</p>
</blockquote>

