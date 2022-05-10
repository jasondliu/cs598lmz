import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
The error is:
<code>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-12-0b7c2b9d4d8c&gt; in &lt;module&gt;()
----&gt; 1 ctypes.cast(0, ctypes.py_object)

/usr/lib/python2.7/ctypes/__init__.pyc in cast(obj, typ)
    331     """
    332     return _cast(obj, typ, False)
--&gt; 333 
    334 def POINTER(typ):
    335     """

TypeError: expected LP_c_long instance instead of int
</code>
When I try to cast <code>ctypes.py_object</code> to <code>ctypes.c_long</code> I get a similar error:
<code>ctypes.cast(ctypes.py_object, ctypes.c_long)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
