import ctypes
ctypes.cast(0, ctypes.py_object).value
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.4/ctypes/__init__.py", line 434, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python3.4/ctypes/__init__.py", line 439, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: function 'value' not found
</code>
What am I doing wrong?


A:

The <code>ctypes.py_object</code> type is not a pointer type.  You can't cast to it.  You can only cast from it.
<code>&gt;&gt;&gt; ctypes.cast(0, ctypes.py_object)
Traceback (most recent call last):
  File
