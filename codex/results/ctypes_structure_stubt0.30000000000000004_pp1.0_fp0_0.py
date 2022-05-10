import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x, s.y
</code>
The output is:
<code>1 0
</code>
Why is the value of <code>s.y</code> 0?


A:

<code>ctypes.c_int()</code> returns an instance of <code>c_int</code> with value 0.
<code>&gt;&gt;&gt; ctypes.c_int()
c_int(0)
</code>
You need to use <code>ctypes.c_int(0)</code> to get an instance of <code>c_int</code> with value 0.
<code>&gt;&gt;&gt; ctypes.c_int(0)
c_int(0)
</code>

