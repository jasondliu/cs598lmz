import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 4
s.y = 5

# This doesn't work
s.x.value = 3
</code>
Is there any way to set the value of a <code>c_int</code> object?


A:

I'm afraid there's no way to do it. <code>ctypes</code> treats a <code>c_int</code> as a structure with a single field called <code>value</code>. This can be seen by asking <code>ctypes</code> to print out a <code>c_int</code> object:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.c_int(1)
c_int(1)
</code>
From this we know that the <code>c_int</code> type contains a single <code>value</code> field which can be accessed like this:
<code>&gt;&gt;&gt; ctypes.c_int
