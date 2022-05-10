import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s)
</code>
Output:
<code>1
2
&lt;__main__.S object at 0x7f3f9c8a9d50&gt;
</code>

<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s)
</code>
Output:
<code>1
2
&lt;__main__.S object at 0x7f2c9c8a9d50&gt;
</code>

<code>import ctypes

class S(ctypes.Structure):
    _fields
