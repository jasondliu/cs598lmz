import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
This works, but I don't want to use ctypes. I would like to use cffi.
I tried this:
<code>from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef ... fun_t;
""")
lib = ffi.dlopen("libc.so.6")
fun = lib.fun
fun()
</code>
But I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    fun = lib.fun
  File "/usr/local/lib/python2.7/dist-packages/cffi/api.py", line 679, in __getattr__
    raise AttributeError(name)
AttributeError: fun
</code>
Any idea how to do this?


A:

You have to use <code>ffi.cast</code> to cast the function pointer to the correct type.
<code>from cffi import
