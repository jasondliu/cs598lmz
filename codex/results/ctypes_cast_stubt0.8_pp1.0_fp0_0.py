import ctypes
ctypes.cast(2748.0, minPos)

x = "xyz"
ctypes.cast(x, minPos)
</code>
I got this error message:
<code>Traceback (most recent call last):
  File "C:\Users\rkna\Desktop\ctypes_test.py", line 13, in &lt;module&gt;
    ctypes.cast(x, minPos)
ctypes.ArgumentError: ctypes.cast() arg 2 must be a ctypes type
</code>
Couldn't find any helpful tutorials or documentation on this specific error message. What am I doing wrong?

