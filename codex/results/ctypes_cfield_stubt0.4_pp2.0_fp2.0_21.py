import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __getattribute__(self, name):
        print "getattr", name
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        print "setattr", name, value
        return object.__setattr__(self, name, value)

c = C()
c.x = 1
print c.x

c.x = S.x
print c.x
</code>
Output:
<code>setattr x 1
getattr x
1
setattr x &lt;Field type=c_int, ofs=0, size=4&gt;
getattr x
&lt;Field type=c_int, ofs=0, size=4&gt;
</code>

