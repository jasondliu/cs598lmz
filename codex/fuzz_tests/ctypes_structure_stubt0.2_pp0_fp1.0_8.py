import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s2 = S()
s2.x = 3
s2.y = 4

print s2.x, s2.y

print s.x, s.y
</code>
The output is:
<code>1 2
3 4
1 2
</code>
I would expect the last line to be <code>3 4</code> instead of <code>1 2</code>.
I'm using Python 2.7.3 on Windows 7.


A:

The problem is that you are using the same type for both <code>s</code> and <code>s2</code>.  When you change the type of <code>s2</code>, you are changing the type of <code>s</code> as well.
<code>&gt;&gt;&gt; s = S()
&gt;&gt;&gt; s2 = S()
&gt;&
