import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return dict(abc=123)
print fun.__code__
</code>
prints
<code>&lt;code object fun at 0x7fe1077cb3d0, file "test2.py", line 5&gt;
</code>
The <code>__code__</code> signature is:
<code>Signature: fun(*args, **kwargs)
File:      test2.py
Source:   
    @FUNTYPE
    def fun():
        return dict(abc=123)
</code>
The last <code>Source:</code> line is a bit misleading because in fact the function is defined by ctypes. 
The <code>__code__</code> object of <code>print()</code> is:
<code>&lt;code object &lt;module&gt; at 0x7fe1077c3640, file "test2.py", line 7&gt;
</code>
but there is no <code>Source:</code> info. If I add a docstring of <code>print()</code>, inspect.getsource(print) finds
