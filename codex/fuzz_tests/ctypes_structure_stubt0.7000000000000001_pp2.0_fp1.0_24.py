import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte()
    _fields_ = [("x", ctypes.c_ubyte)]
S.x.__doc__="hi"

ctypes.c_ubyte.__doc__="hi"

#S.x.__doc__="hi"

ctypes.c_ubyte.__name__="hi"

print S().x
</code>
However, I was unable to find anything useful in the documentation.
Edit:
I added <code>ctypes.c_ubyte.__doc__="hi"</code> and <code>ctypes.c_ubyte.__name__="hi"</code> to the example to show that I can set the doc or name of the class.


A:

You can do it, but it's not accessible in the usual way:
<code>&gt;&gt;&gt; class S(ctypes.Structure):
...     x = ctypes.c_ubyte()
...     _fields_ = [("x", ctypes.c_ubyte)]
...
