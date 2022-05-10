import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
module = ctypes.CDLL("./dyn_load.so")
foo_func = FUNTYPE(("foo", module))
foo_func(1)
</code>
And it works as expected. It prints <code>foo called with 1</code> on stdout.

