import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 1
</code>
and it works.
But, if I change the last line to <code>return 1.0</code> or <code>return 1.0j</code>, it raises a TypeError: "expected c_double_Array_1 instance, not float" or "expected c_double_Array_2 instance, not complex".
Why is that? In particular, why does the interpreter  think I am trying to return an array of doubles? Does it have something to do with the fact that I am using the <code>ctypes</code> module?

