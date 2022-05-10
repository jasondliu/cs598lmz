import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return "hello world"
</code>
Alternatively, you can use a <code>ndpointer</code> as a return value.
<code>from ctypes import c_char_p, CFUNCTYPE
FUNTYPE = CFUNCTYPE(c_char_p)
fun = FUNTYPE(lambda: "hello world")
</code>
These two function types are roughly equivalent to the following in C:
<code>void*fun() {
  ...
}

char*fun() {
  ...
}
</code>
Be sure to read my guide to ctypes and pointers, especially the section Using the return value of a foreign function.

