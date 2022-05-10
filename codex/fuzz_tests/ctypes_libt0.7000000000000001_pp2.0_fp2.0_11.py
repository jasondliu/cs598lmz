import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
I got the following error:
<code>Traceback (most recent call last):
  File "C:/Users/idana/PycharmProjects/untitled/gui.py", line 3, in &lt;module&gt;
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
  File "C:\Users\idana\AppData\Local\Programs\Python\Python38-32\lib\ctypes\__init__.py", line 380, in __getattr__
    func = self.__getitem__(name)
  File "C:\Users\idana\AppData\Local\Programs\Python\Python38-32\lib\ctypes\__init__.py", line 385, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: function 'MessageBoxW' not found
</code>
I tried also with the <code>windll
