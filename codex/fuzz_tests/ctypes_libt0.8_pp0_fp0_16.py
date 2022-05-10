import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello world!", "My first GUI with Python!", 0)
</code>
But if I replace Windows with Ubuntu and change the message box parameters accordingly, I get this error:
<code>Traceback (most recent call last):
  File "hello_world.py", line 3, in &lt;module&gt;
    ctypes.cdll.LoadLibrary("libc.so.6")
  File "/usr/lib/python3.6/ctypes/__init__.py", line 427, in LoadLibrary
    return self._dlltype(name)
  File "/usr/lib/python3.6/ctypes/__init__.py", line 349, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libc.so.6: cannot open shared object file: No such file or directory
</code>
How do I fix this?


A:

You should use <code>gtk3</code> to make GUI in Python on Ubuntu.
Install pygobject:
<code>sudo
