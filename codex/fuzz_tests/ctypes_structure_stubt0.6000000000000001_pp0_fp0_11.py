import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    def __init__(self):
        self.x = 1
        self.y = 2
s = S()
print s.x
print s.y
</code>
Output:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print s.x
AttributeError: 'S' object has no attribute 'x'
</code>


A:

<code>ctypes.Structure</code> is intended for interfacing with C types. You can't use it to create your own types. If you want to create your own type, use <code>type</code>.
<code>&gt;&gt;&gt; def S():
...     x = 1
...     y = 2
... 
&gt;&gt;&gt; s = S()
&gt;&gt;&gt; s.x
1
&gt;&gt;&gt; s.y
2
</code>

