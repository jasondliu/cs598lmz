import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
func = FUNTYPE(lambda: None)
</code>
The generated function pointer type is:
<code>&lt;class '_ctypes.CFuncPtrType'&gt;
</code>
This is a subtype of <code>ctypes._CFuncPtr</code>, which is itself a subtype of <code>ctypes.Structure</code>.
<code>&gt;&gt;&gt; ctypes.CFuncPtrType.__mro__
(&lt;class '_ctypes.CFuncPtrType'&gt;,
 &lt;class 'ctypes._CFuncPtr'&gt;,
 &lt;class 'ctypes.Structure'&gt;,
 &lt;class 'ctypes._SimpleCData'&gt;,
 &lt;class 'ctypes.CData'&gt;,
 &lt;class 'object'&gt;)
</code>
The <code>ctypes.Structure</code> class has an instance method <code>from_address</code> which will return a Python object wrapping the address provided.
<code>&
