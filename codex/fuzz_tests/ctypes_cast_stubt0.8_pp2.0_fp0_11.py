import ctypes
ctypes.cast(ctypes.c_void_p, ctypes.py_object)
</code>
This raises the error:
<code>TypeError: 'instancemethod' object is not callable
</code>
I took a look at the Python sourcecode and found that the <code>cast</code> function is defined as:
<code>def cast(obj, typ):
    """Cast an object to a type. This implements what you get from
    casting in C, regardless of the current language.
    """
    return obj._as_parameter_
</code>
And <code>_as_parameter_</code> is a method of the <code>_ctypes._SimpleCData</code> class (which is the base class of all ctypes types).
Why can't I cast a <code>ctypes.py_object</code> to itself?


A:

The <code>py_object</code> type is just an alias for <code>c_void_p</code>; it's not an actual type. Therefore, you don't need to cast it at all.

