import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S()
print s.x, s.y
print s.__dict__
assert "x" in s.__dict__
assert "y" in s.__dict__
s.x = 1
s.y = 2
print s.x, s.y
</code>
The output is:
<code>0 0
{'y': &lt;Field type=c_int, ofs=4, size=4&gt;, 'x': &lt;Field type=c_int, ofs=0, size=4&gt;}
1 2
</code>


A:

There's no magic about it. The <code>__dict__</code> is a normal attribute of the object.
The dictionary is created when the object is created.
When you access an attribute, the <code>__getattribute__</code> method is invoked. <code>__getattribute__</code>
