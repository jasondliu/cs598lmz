import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return None
print fun
</code>
The output was:
<code>&lt;__main__.fun_type object at 0x7f96450179d8&gt;
</code>
What is this object? Can I convert the object to a callable?


A:

That's the class object of your <code>FUNTYPE</code> type object.
Yes, you can convert it to a callable: just call it:
<code>python -c 'import ctypes;FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object); @FUNTYPE;def fun(): return None; print(fun); print(fun.__call__ is fun)'
&lt;__main__.fun_type object at 0x7fd28b7f8410&gt;
True
</code>
Note that <code>__call__</code> isn't special; the <code>instance.__class__.__call__(instance, *a, **kw)</code> call above is equivalent to just <code>instance(*a, **kw)</code>.

