import ctypes
ctypes.cast(p, ctypes.py_object).value = 10
print(q)

# This doesn't work.
ctypes.cast(p, ctypes.py_object).value = None
print(q)
 
</code>
The error message is:
<code>Traceback (most recent call last):
  File "problem_4.py", line 14, in &lt;module&gt;
    ctypes.cast(p, ctypes.py_object).value = None
  File "C:\Users\naadu\Anaconda3\lib\ctypes\__init__.py", line 374, in __setattr__
    self._handle = _dlopen(self._name, mode)
OSError: [WinError 126] The specified module could not be found
</code>
Update
Nevermind. The documentation says the following:
<blockquote>
<p>Using the ctypes module it is possible to pass (or return) arbitrary data as a pointer and cast it to a ctypes instance in order to access its fields. However, this is a hack, and it only works for accessing a few
