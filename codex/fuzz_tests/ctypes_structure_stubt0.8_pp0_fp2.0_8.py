import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print 'before:', s.x, s.y
s.x = 4; s.y = 5
print 'after:', s.x, s.y
</code>
When run under Python 2.x I get what I expect:
<code>$ python2 test.py
before: 0 0
after: 4 5
</code>
But under Python 3.x, I get something that I don't understand:
<code>$ python3 test.py
before: 4224 0
after: 4 5
</code>
It's as though the first time <code>s</code> is accessed, I'm just getting some random junk that happens to be in <code>s</code>'s memory.  I'm not sure why this is happening.  I've tried looking at the C source code for Python 3.x, but it's a bit overwhelming for me.
I'm also wondering if anybody can explain to me what's happening under the hood here.  I know that <code>ctypes</code> is a
