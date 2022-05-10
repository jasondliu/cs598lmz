import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun()
</code>
The above code works fine with Python 2.7.13, but it crashes with Python 3.6.3:
<code>Fatal Python error: PyThreadState_Get: no current thread
</code>
I've tried to debug it with gdb and it seems that the problem is in the <code>PyEval_EvalFrameEx</code> function in <code>ceval.c</code>, which is called from <code>PyEval_EvalCodeEx</code> in <code>Python/ceval.c</code> (which is called from <code>PyEval_EvalCode</code>).
The <code>PyEval_EvalFrameEx</code> function is called with a <code>PyFrameObject</code> that has a <code>f_exc_type</code> and a <code>f_exc_value</code> that are both <code>NULL</code>. It then calls <code>PyThreadState_GET()</code> and gets a <code>NULL</code> pointer.
The <code>PyEval
