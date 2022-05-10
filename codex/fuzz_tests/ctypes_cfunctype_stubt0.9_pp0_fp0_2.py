import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "test"
ctypes.pythonapi.PyCode_New(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ctypes.pythonapi.PyEval_EvalCode(ctypes.py_object(fun).func_code, gl, gl)
</code>
Ok, so let's try <code>PyCode_New</code> and then <code>PyEval_EvalCode</code> and see what happens!
On Python 2.4.6, I get a segfault.
<code>Segmentation fault (core dumped)
</code>
On Python 2.6.9, I get a hash table error.
<code>Fatal Python error: PyEval_RestoreThread: NULL tstate
</code>
And on Python 3.4.3, we get a fatal error.
<code>Fatal Python error: unexpected exception during garbage collection
</code>

PyRun_String
Wait a minute! I tried to use <code>PyRun_String</code>, not <code>PyEval_</code>!
