import ctypes
ctypes.cast(a, ctypes.c_void_p).value
Out[9]: 139958021018224
</code>
Now if you install the <code>cython</code> module you can get this all in one line:
<code>In [10]: import cython
In [11]: cython.cast(a, 'void *').value
Out[11]: 139958021018224
</code>

