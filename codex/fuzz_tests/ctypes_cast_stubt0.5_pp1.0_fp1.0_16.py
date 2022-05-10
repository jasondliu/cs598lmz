import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
The error is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ctypes/__init__.py", line 366, in cast
    return _cast(obj, _type)
TypeError: must be a ctypes type
</code>
What does this error mean?


A:

You need to use the <code>py_object</code> type from <code>ctypes</code>:
<code>ctypes.cast(0, ctypes.py_object)
</code>

