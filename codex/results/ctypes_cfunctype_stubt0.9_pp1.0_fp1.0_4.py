import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): print 'hello world!'; return 2
new_f = fun.ctypes.fptr
print new_f
</code>
which gives
<code>%&gt; python test.py 
&lt;_CFuncPtr object at 0x121858c40&gt;
</code>

