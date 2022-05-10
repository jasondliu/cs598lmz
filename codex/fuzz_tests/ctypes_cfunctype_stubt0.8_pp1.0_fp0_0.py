import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'hello'
print fun()
&lt;__main__.CFUNCTYPE object at 0x00DDA250&gt;
</code>

