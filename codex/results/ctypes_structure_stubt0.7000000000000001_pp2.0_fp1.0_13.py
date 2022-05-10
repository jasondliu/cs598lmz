import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte(1)
    y = ctypes.c_ubyte(2)

s = S()
print(s.x)
print(s.y)
print(type(s.x))
print(type(s.y))
print(type(s))
</code>
Output:
<code>1
2
&lt;class 'int'&gt;
&lt;class 'int'&gt;
&lt;class '__main__.S'&gt;
</code>

