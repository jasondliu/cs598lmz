import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

s = S()
print(type(s.x), s.x)
print(type(s.y), s.y)

# &lt;class 'int'&gt; 0
# &lt;class 'float'&gt; 0.0
</code>
The reason I'm asking is that I'm trying to use the <code>ctypes</code> module to modify a binary file, and I want to know what type to expect for each field in the binary file.


A:

There is no reason for the <code>ctypes</code> types to behave this way. 
<code>&gt;&gt;&gt; class Uninitialized(ctypes.Structure):
...     _fields_ = [('x', ctypes.c_int)]
... 
&gt;&gt;&gt; u = Uninitialized()
&gt;&gt;&gt; u.x
0
</code>
<code>ctypes</code> doesn't have an <code>__init__</code> method
