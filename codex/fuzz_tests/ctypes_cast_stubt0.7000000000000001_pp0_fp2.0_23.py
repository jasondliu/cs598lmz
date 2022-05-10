import ctypes
ctypes.cast(0x1, ctypes.py_object).value
</code>
And on Python 3:
<code>&gt;&gt;&gt; (id(1), id(True))
(4349288800, 4349288800)
</code>

