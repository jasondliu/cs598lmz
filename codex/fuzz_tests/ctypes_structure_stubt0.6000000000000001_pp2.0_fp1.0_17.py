import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class W(ctypes.c_void_p):
    def __init__(self, *args, **kwargs):
        super(W, self).__init__(*args, **kwargs)
        self.s = S()

w = W()
w.s.x = 3
print w.s.x, w.s.y
</code>
It prints <code>3 2</code>, but I want it to print <code>3 1</code> (the default value of <code>y</code>). How should I do it?


A:

You can't do it that way, but you can do it this way:
<code>class W(ctypes.c_void_p):
    def __init__(self, *args, **kwargs):
        super(W, self).__init__(*args, **kwargs)
        self
