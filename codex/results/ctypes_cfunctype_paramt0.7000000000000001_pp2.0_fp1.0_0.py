import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(x):
    print(x)

mylib = ctypes.cdll.LoadLibrary('./libmylib.so')
mylib.register_callback(FUNTYPE(callback))
mylib.run_callback()
</code>
I get the error:
<code>Traceback (most recent call last):
  File "./test.py", line 13, in &lt;module&gt;
    mylib.run_callback()
OSError: exception: access violation reading 0x00000000000000E8
</code>
However, if I make the function I pass to <code>register_callback</code> return a random integer, then it works.  If I change the C code to call <code>printf</code> on the value it gets from the callback, it works.  So the error seems to be in how Python is handling the return value from the callback, in combination with how the C code is processing it.  I assume the former happens in <code>Python/ceval.c</code>, but I'm not sure where to start looking
