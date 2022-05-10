import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
I got this error:
<code>Traceback (most recent call last):
  File "C:\Users\User\Desktop\test.py", line 2, in &lt;module&gt;
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\ctypes\__init__.py", line 348, in __getattr__
    func = self.__getitem__(name)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\ctypes\__init__.py", line 353, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: function 'MessageBoxW' not found
</code>
I tried to install <code>pywin32</code> but it doesn't solve the problem.
