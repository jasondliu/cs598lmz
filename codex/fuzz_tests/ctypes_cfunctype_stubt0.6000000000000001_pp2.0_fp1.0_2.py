import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    #Do some stuff
    return some_object
</code>
The call from C++ looks like this:
<code>PyObject *py_fun = PyObject_GetAttrString(module, "fun");
PyObject *ret = PyObject_CallObject(py_fun, NULL);
</code>
In a normal python script, this works fine, but when running it from a custom interpreter, it gives a segmentation fault.
I have tried running it with gdb, but it doesn't give any useful information.
<code>Thread 1 "python" received signal SIGSEGV, Segmentation fault.
0x00007ffff7def5f3 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
(gdb) bt
#0  0x00007ffff7def5f3 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007ffff7dd9fc0 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#2  0x00007ffff7
