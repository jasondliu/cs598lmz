import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int, ctypes.c_int)

def wrapper(out, state):
    out = out.value
    state = state.value
    print(out, state)

cfunc = FUNTYPE(wrapper)

# ctypes.cast(cfunc, ctypes.c_void_p)
lib.set_callback(cfunc)
</code>
But I get the error:
<code>Traceback (most recent call last):
  File "d:/Python/bipc_test/test4.py", line 14, in &lt;module&gt;
    lib.set_callback(cfunc)
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1
</code>
I have tried casting the cfunc in various ways but I always get something like "to c_void_p" error.
I think that I'm using the ctypes.CFUNCTYPE function wrong but I'm not sure.

