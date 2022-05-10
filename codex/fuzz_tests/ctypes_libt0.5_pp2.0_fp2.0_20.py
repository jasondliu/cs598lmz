import ctypes
ctypes.windll.user32.MessageBoxA(0, 'Hello, World!', 'Python', 1)
</code>
I get the error:
<code>Traceback (most recent call last):
  File "&lt;pyshell#1&gt;", line 1, in &lt;module&gt;
    ctypes.windll.user32.MessageBoxA(0, 'Hello, World!', 'Python', 1)
  File "C:\Python27\lib\ctypes\__init__.py", line 378, in __getattr__
    func = self.__getitem__(name)
  File "C:\Python27\lib\ctypes\__init__.py", line 383, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: function 'MessageBoxA' not found
</code>
What am I doing wrong?
I'm using Python 2.7.3 on Windows 7 64-bit.


A:

I found the answer to this by looking at the source code of the <code>win32gui
