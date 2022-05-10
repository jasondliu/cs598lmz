import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class C(object):
    def __init__(self):
        self.fun = fun
</code>
I can call this function from C++, but I can't call it from python.
<code>&gt;&gt;&gt; c = C()
&gt;&gt;&gt; c.fun()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'PyCFunctionObject' object is not callable
</code>
I can call it from python if I use <code>ctypes.CFUNCTYPE(ctypes.c_char_p)</code> instead of <code>ctypes.CFUNCTYPE(ctypes.py_object)</code>.
I can also call it from python if I use <code>ctypes.CFUNCTYPE(ctypes.c_char_p)</code> and return a <code>ctypes.c_char_p</code> instead of a string.
<code>&gt;&
