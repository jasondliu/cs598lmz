import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   print("xx")
x = fun()
</code>
Python complains, giving this error:
<blockquote>
<p>TypeError: object of type 'CFUNCTYPE' has no len()</p>
</blockquote>
Any pointers?


A:

File size is a characteristic of the data written to a file, not an attribute of the <code>file</code> object itself.
That's also why <code>__len__</code> or <code>__sizeof__</code> would not work with a file object directly: one would have to somehow read the file and return its size in bytes.

