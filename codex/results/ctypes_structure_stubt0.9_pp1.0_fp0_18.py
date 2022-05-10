import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong
    z = ctypes.c_longlong

def f(s):
    return (s.x, s.y, s.z)

def access_to_instance_attr():
    s = S(1,2,3)
    return f(s)

print(access_to_instance_attr())
</code>
With cpython v3.5.2 I get:
<code>(1, 2, 3)
</code>
This is what I would expect.
However, with pypy3 v6.0 I get:
<code>(1, 0, 0)
</code>
Unfortunately, pypy3 is the python version that I need to use.
Why does this happen? What can I do to obtain the expected result in pypy?
(Not that it makes any difference, but I'm running pypy on aarch64, ubuntu 18.04.)


A:

The <code>.z</code> member of the <code>S</code> structure does not start at
