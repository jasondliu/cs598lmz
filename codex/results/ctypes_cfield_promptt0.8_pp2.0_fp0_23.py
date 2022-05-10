import ctypes
# Test ctypes.CField
# http://docs.python.org/library/ctypes.html#id1

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

print Point.x
# Traceback (most recent call last):
#   File "pydevd.py", line 567, in &lt;module&gt;
#     execfile(file, globals, locals) # execute the script
#   File "C:/alan/eclipse_workspace/test_ctypes/pydevd.py", line 20, in &lt;module&gt;
#     print Point.x
# AttributeError: type object 'Point' has no attribute 'x'
</code>
Why does this give an error?  Isn't the '_fields_' supposed to make it add the x and y fields to the object? 


A:

You need to create an instance of the structure first:
<code>p = Point()
print p.x
</code>
Or, you can use an anonymous
