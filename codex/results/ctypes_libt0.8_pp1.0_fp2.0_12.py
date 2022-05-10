import ctypes
ctypes.cast(cp, ctypes.py_object).value
</code>
which gives you:
<code>&lt;__main__.Class at 0x1f50d28&gt;
</code>
This method is not deprecated, but deprecated and still available functions are also displayed in the documentation, so you can also use
<code>cp = ctypes.py_object(c)
</code>

