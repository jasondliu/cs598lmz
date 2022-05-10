import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def my_callback(x): print("Callback invoked with value", x)
ctypes.cast(FUNTYPE(my_callback), ctypes.c_void_p).value
</code>
Which looks like it should work, but doesn't:
<code>&gt;&gt;&gt; ctypes.cast(FUNTYPE(my_callback), ctypes.c_void_p).value
0
</code>
What am I missing?


A:

When you create a callback, libffi creates a trampoline function that will call your Python function.  The trampoline is created on libffi's memory.  You can't get the address of it because libffi doesn't expose it.
Just make a C function that calls the libffi trampoline and pass that to your function.

