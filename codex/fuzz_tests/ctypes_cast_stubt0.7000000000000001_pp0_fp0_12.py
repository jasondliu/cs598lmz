import ctypes
ctypes.cast(int(addr), ctypes.py_object).value
</code>
This is the final result:
<code>&gt;&gt;&gt; a = 10
&gt;&gt;&gt; hex(id(a))
'0x1866b88'
&gt;&gt;&gt; ctypes.cast(int(0x1866b88), ctypes.py_object).value
10
</code>

