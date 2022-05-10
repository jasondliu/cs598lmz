import ctypes
ctypes.cast(p, ctypes.py_object).value
</code>
so in this case you may be able to get away with:
<code>def get_pointer_to_object(ob):
    return ctypes.cast(id(ob), ctypes.py_object).value
</code>
But there are also non-Python objects in CPython that have a <code>PyObject</code> structure:
<code>&gt;&gt;&gt; import _sqlite3
&gt;&gt;&gt; _connection = _sqlite3.connect(":memory:")
&gt;&gt;&gt; id(_connection)
1347076704
&gt;&gt;&gt; type(_connection)
&lt;class '_sqlite3.Connection'&gt;
&gt;&gt;&gt; ctypes.cast(id(_connection), ctypes.py_object).value
&lt;_sqlite3.Connection object at 0x109c41640&gt;
</code>
If the object you want to find is the top-level object, you cannot reliably search for
