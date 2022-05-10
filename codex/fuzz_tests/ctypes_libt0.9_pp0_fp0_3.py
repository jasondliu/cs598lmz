import ctypes
ctypes.windll.user32.MessageBoxW(0, u"Hello world!", u"Test", 1)
</code>
and got the error:
<code>Traceback (most recent call last):
  File "...\Desktop\Desktop.py", line 2, in &lt;module&gt;
    ctypes.windll.user32.MessageBoxW(0, u"Hello world!", u"Test", 1)
  File "C:\python26\lib\ctypes\__init__.py", line 365, in __getattr__
    func = self.__getitem__(name)
  File "C:\python26\lib\ctypes\__init__.py", line 370, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: function 'MessageBoxW' not found
</code>
I know that the function is present in <code>user32.dll</code> from <code>windll</code>, so why did I get that error?
I've also tried to use <code>ctypes.cdll.user32.
