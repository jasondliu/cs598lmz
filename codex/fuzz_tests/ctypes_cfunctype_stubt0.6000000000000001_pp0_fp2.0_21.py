import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

fun()
</code>
Here, I am getting a segmentation fault.
<code># python3 -c 'import ctypes; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object); @FUNTYPE; def fun(): return None; fun()'
Segmentation fault
</code>
I am getting this on both Ubuntu and Mac OS X.
<code>$ python3 --version
Python 3.5.2

$ python3 -c 'import sys; print(sys.platform)'
darwin
</code>
What is the problem?


A:

This is a known bug in Python 3.5.2. It was fixed in Python 3.5.3.

