import ctypes
ctypes.cast(0, ctypes.py_object)

# Output:
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "ctypes/__init__.py", line 365, in cast
    return _cast(obj, type)
TypeError: must be a ctypes type

</code>
I'm trying to understand how is casting done in Python, as it is not available with <code>ctypes</code> as well.


A:

I think what you're looking for is something like this:
<code>import ctypes

class foo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint8),
                ("b", ctypes.c_int8)]


val = 0x12345678

f = foo()

ctypes.cast(ctypes.byref(f), ctypes.POINTER(ctypes.c_uint8))[0] = val

print(f.a)
print(f.b)
</code
