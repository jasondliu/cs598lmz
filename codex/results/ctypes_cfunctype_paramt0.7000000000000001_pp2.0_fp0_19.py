import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
# x86_64-w64-mingw32-gcc -shared -Wl,--subsystem,windows -o dll.dll dll.c

dll = ctypes.WinDLL('dll.dll')
dll.DllFunc.argtypes = (FUNTYPE,)
dll.DllFunc.restype = None

def foo():
    print('foo')

foo_cb = FUNTYPE(foo)
dll.DllFunc(foo_cb)
</code>
But, this gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 17, in &lt;module&gt;
    dll.DllFunc(foo_cb)
ValueError: Procedure probably called with too many arguments (4 bytes in excess)
</code>
How do I pass a function pointer to my DLL?
Thanks in advance!


A:

On 64-bit python, <code>FUNTYPE</code> is <code>ctypes.WINFUNCTYPE(None)</code> which has the following signature
