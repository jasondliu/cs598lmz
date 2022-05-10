import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    print(S.x)
    print(type(S.x))
    print(S.x.__class__)

test()
</code>
The output is:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
&lt;class 'ctypes.CField'&gt;
</code>
As you can see, <code>S.x</code> is an instance of <code>CField</code>, and <code>S.x.__class__</code> is <code>CField</code>.

