import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16(65535)
    y = ctypes.c_int64(0)
    z = ctypes.c_uint8(255)

    def __init__(self):
        super(S, self).__init__()
        self.y = 0
        self.z = 255

a = S()

print a.x , a.y, a.z
</code>
Output
<code>65535 0 255
</code>
This is the same code run on my iPython console:

Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
Type "copyright", "credits" or "license" for more information.

IPython 0.10 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: run /Users/myusername/Documents/test.py
65535 0
