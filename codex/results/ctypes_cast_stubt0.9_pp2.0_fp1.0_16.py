import ctypes
ctypes.cast(id(a), ctypes.py_object).value
Out[2]: 3
</code>
To get the reference count, you would use:
<code>ctypes.cast(id(a), ctypes.py_object).ob_refcnt
</code>
But you can't create a 'strong reference' to an integer like this. It is unpacking the pointer to the <code>long_object</code> from <code>py_object.cval</code> (or <code>cdata</code> attribute in Python 3).

