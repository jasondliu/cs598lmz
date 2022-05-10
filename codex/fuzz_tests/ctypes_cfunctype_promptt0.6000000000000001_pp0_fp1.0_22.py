import ctypes
# Test ctypes.CFUNCTYPE()

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
def func(arg):
    print(arg[0])
    return 0

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.printf(b"Hello %s\n", b"World")

cfunc = prototype(func)
cfunc(ctypes.pointer(ctypes.c_int(42)))
</code>
I get the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    cfunc(ctypes.pointer(ctypes.c_int(42)))
TypeError: argument 1 must be a character buffer object
</code>
It seems that <code>ctypes.POINTER(ctypes.c_int)</code> is a <code>int</code>, not <code>char*</code>.
I also tried to use <code>cfunc = prototype(func.en
