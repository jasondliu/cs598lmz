import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print(type(s.x))
print(type(s.y))

s.x = 1
s.y = 2
print(s.x, s.y)
</code>
Output:
<code>&lt;class 'ctypes.c_int'&gt;
&lt;class 'ctypes.c_int'&gt;
1 2
</code>
But I am looking for something like this:
<code>class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(type(s.x))
print(type(s.y))

s.x = 1
s.y = 2
print(s.x, s.y)
</code>
Output:
<code>&lt;class 'ctypes.c_int'&gt;
&lt;class 'ctypes.c_int'&gt;
1 2
</code>
