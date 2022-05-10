import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
</code>
The error message is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 1, in fun
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1
</code>
Python 3.7.1. 
I had a look at the source code and it seems that <code>ctypes.py_object</code> is intended to be a valid return type, but it seems to be silently ignored when it is used as a return type.
This is the relevant code I found in <code>/usr/lib/python3.7/ctypes/__init__.py</code>:
<code>class _SimpleCData(_CData):
    _type_ = "c"
    #_is_pointer_like = False
    _is_ref_like = False
    def _check_retval_(self):
        #
