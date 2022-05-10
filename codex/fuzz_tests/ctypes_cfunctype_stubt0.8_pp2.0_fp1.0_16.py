import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

EXPORT = [('fun', fun),]
</code>
It returns the correct value, but I cannot use any other function from the ctypes library. When I try to execute, I get an ImportError:
<code>$ python test.py
Traceback (most recent call last):
  File "test.py", line 2, in &lt;module&gt;
    import ctypes
ImportError: /tmp/_ctypes.so: invalid ELF header
</code>
This error occurs immediately after importing ctypes, before <code>fun</code> is ever defined or used. This error does not occur when I remove the <code>import ctypes</code> line.
I am aware of the <code>CFFI_USE_PYCC</code> environment variable, but it does not appear to solve this problem. It only ensures that ctypes is properly imported. I am looking for a way to allow the use of other ctypes functions, not just their inline declarations.
Is there a way to use ctypes functions in CFFI without having to import ctypes?


A:

The problem was that
