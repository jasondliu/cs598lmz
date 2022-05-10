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
Output:
<code>1 2
3 4
1 2
</code>
I would expect the last line to be <code>3 4</code> as well.
What am I missing?


A:

You are creating two instances of <code>S</code>, <code>s</code> and <code>s2</code>.  The <code>x</code> and <code>y</code> attributes of <code>s</code> are not the same as the <code>x</code> and <code>y</code> attributes of <code>s2</code>.  You can see this by printing the addresses of the two instances:
<code>print id(s), id(s2
