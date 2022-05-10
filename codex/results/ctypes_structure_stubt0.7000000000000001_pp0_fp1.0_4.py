import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double

class A(object):
    def __init__(self):
        self.s = S()
        self.s.x = 3

a = A()

print a.s.x
</code>
This gives a segfault.  What am I doing wrong?


A:

The <code>__getattr__</code> and <code>__setattr__</code> methods in <code>ctypes.Structure</code> are only called for items that aren't already present in the object's <code>__dict__</code>, whereas <code>x</code> is.  The solution is to call the <code>S</code> class initializer (which will populate <code>__dict__</code>):
<code>class A(object):
    def __init__(self):
        self.s = S()
        S.__init__(self.s)
        self.s.x = 3
</code>

