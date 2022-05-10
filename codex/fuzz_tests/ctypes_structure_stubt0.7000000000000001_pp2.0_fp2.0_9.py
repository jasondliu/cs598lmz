import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8

p = multiprocessing.Pool()

s = S()
s.x = 1

def f(s):
    s.x = 2
    return s.x

print(p.map(f, [s]))
</code>
The above code prints <code>[2]</code> as expected.
However, when instead I use
<code>print(p.map(f, [s.x]))
</code>
I get the error
<code>TypeError: expected c_uint8, got int
</code>
This makes sense because <code>s.x</code> is an <code>int</code>, and so <code>[s.x]</code> is a list of <code>int</code>s, but <code>f</code> expects a list of <code>S</code> instances. 
However, it doesn't make sense that
<code>print(p.map(f, [s]))
</code>
works. I would expect that the same problem would occur if I pass in <code>
