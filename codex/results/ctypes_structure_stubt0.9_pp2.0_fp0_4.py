import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int, 1), ('y', ctypes.c_int)]

s = S()
ss = S.y
print (ss)
&gt;&gt;&gt; &lt;Field type=c_int, ofs=1, size=31&gt;
</code>


A:

When you do this:
<code>class T(ctypes.Structure):
    _fields_ = [('foo', ctypes.c_int8),
                ('bar', ctypes.c_int32, 3),
                ('baz', ctypes.c_int8)]
</code>
<code>ctypes</code> creates <code>T</code> with a <code>foo</code> in position #1, a <code>bar</code> in position #4, and a <code>baz</code> in position #5, like this:
<code>[0]   [1]       [2]       [3]      
