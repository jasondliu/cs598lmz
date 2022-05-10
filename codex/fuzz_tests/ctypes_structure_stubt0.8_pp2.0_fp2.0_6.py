import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char*10
    y = ctypes.c_char*10
</code>
Now, I would like to pass a <code>str</code> to <code>x</code> and <code>y</code> fields, but get a <code>TypeError</code>.
I tried this, but I would prefer to avoid the <code>encode</code>/<code>decode</code> steps:
<code>s = S()
s.x = s.y = 'hello'.encode('ascii')
</code>
I tried this, but get a <code>TypeError</code>:
<code>s = S()
s.x = s.y = 'hello'
</code>


A:

You could use a <code>ctypes.c_char * 10</code> as the type for <code>x</code> and <code>y</code>:
<code>from ctypes import *

class S(Structure):
    _fields_ = [('x', c_char * 10),
                ('y', c_char
