import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class S2(S):
    z = 3
    _fields_ = [("z", ctypes.c_int)]

class S3(S2):
    _fields_ = [("a", ctypes.c_int)]

print S().x
print S().y
print S2().x
print S2().y
print S2().z
print S3().x
print S3().y
print S3().z
print S3().a
</code>
Which gives:
<code>1
2
1
2
3
1
2
3
0
</code>
I understand that when I add <code>_fields_</code> to <code>S3</code>, I'm replacing the <code>_fields_</code> attribute inherited from <code>S2</code> (which may or may not have an effect on the class layout).
But why does <code>S3().a</code> return
