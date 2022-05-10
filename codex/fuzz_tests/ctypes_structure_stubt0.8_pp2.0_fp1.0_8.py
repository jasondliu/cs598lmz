import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64(3)
    y = ctypes.c_int64(4)


s = S()

s.x = 2 # &lt;- works
s.y = 2 # &lt;- error: 'c_longlong' object does not support assignment
</code>
The reason seems to be that the latter is done implicitly by the <code>array</code> module when constructing the ctypes array of structures.  And ctypes doesn't allow assignment to <code>c_longlong</code> instances.
The actual error is:
<code>TypeError: 'c_longlong' object does not support assignment
</code>

