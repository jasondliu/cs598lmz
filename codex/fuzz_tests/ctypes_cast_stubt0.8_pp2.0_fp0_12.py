import ctypes
ctypes.cast(obj, ctypes.py_object).value
</code>
Not sure where the <code>NULL</code> is coming from, but the following works just fine with a <code>str</code> object:
<code>In [1]: import ctypes

In [2]: s = 'foo'

In [3]: ctypes.cast(id(s), ctypes.py_object).value == s
Out[3]: True
</code>

