import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
def callback():
    pass
fun.argtypes = (FUNTYPE,)
fun(callback)
</code>
I get:
<code>Traceback (most recent call last):
  File "C:\Users\user1\Desktop\test.py", line 13, in &lt;module&gt;
    fun(callback)
TypeError: in method 'fun', argument 1 of type 'CFUNCTYPE(PyObject * (*)())'
</code>
How can I fix this? I'm using Python 2.7.


A:

You need to use <code>ctypes.WINFUNCTYPE</code> instead of <code>ctypes.CFUNCTYPE</code>.

