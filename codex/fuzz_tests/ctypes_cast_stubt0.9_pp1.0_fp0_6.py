import ctypes
ctypes.cast(p, ctypes.py_object).value
</code>
Gives:
<code>&gt;&gt;&gt; print(ctypes.cast(p, ctypes.py_object).value)
&lt;__main__.C instance at 0x8049c8&gt;
</code>

