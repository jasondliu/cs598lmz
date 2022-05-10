import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print "callback called with", x
    return x

cb = FUNTYPE(my_callback)

lib.call_my_callback(cb)
</code>
When I run this, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    lib.call_my_callback(cb)
ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention
</code>
What am I doing wrong?


A:

You are missing the calling convention, which is <code>cdecl</code> by default but in your case is <code>stdcall</code>.
<code>FUNTYPE = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)
</code>

