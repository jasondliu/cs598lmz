import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]

class S2(S):
    _fields_ = [('y', ctypes.c_int)]

class S3(S2):
    _fields_ = [('z', ctypes.c_int)]

print S3.x
print S3.y
print S3.z
print S3.__dict__['x']
print S3.__dict__['y']
print S3.__dict__['z']

s3 = S3()
print s3.x
print s3.y
print s3.z

s2 = S2()
print s2.x
print s2.y

s = S()
print s.x
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;Field type=c_int, ofs=4, size=4&gt;
&lt;Field type=c_int, ofs=8, size=
