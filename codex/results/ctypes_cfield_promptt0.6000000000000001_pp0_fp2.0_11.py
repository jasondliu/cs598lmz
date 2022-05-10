import ctypes
# Test ctypes.CField class

# First, create a simple structure
class X(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

# Now, try to create a Field object
f = ctypes.CField(ctypes.c_int, "foo", X, 0)
print(f)

# Now, try to create a Field object
f = ctypes.CField(ctypes.c_int, "foo", X, 1)
print(f)
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
Traceback (most recent call last):
  File "C:\Users\user\Desktop\ctypes-test.py", line 11, in &lt;module&gt;
    f = ctypes.CField(ctypes.c_int, "foo", X, 1)
  File "C:\Users\user\AppData\Local\Programs\Python\Python38\lib\ctypes\__init__.py", line 721, in __init__
    raise Value
