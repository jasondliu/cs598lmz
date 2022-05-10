import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def show(argcount=0):
    code = compile("def f(" + (", x" * argcount) + "): return x", "", "exec")
    frame = ctypes.pythonapi.PyFrame_New(ctypes.pythonapi.PyThreadState_Get(),
                                         code,
                                         {},
                                         {})
    ctypes.pythonapi.PyFrame_FastToLocals(frame)
    for name, locals in frame.f_locals.items():
        print(name, type(locals))
    for i in range(argcount):
        cb = ctypes.CFuncPtr(show)
        locals.__call__(argcount - 1)

show(3)
</code>
Output:
<code>f &lt;class 'pythonapi.PyCFunctionObject'&gt;
x &lt;class 'ctypes.CField'&gt;
x &lt;class 'ctypes.CField'&gt;
x &lt;class 'ctypes.CField'&gt;
f &lt;class 'pythonapi.
