import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_void_p)

def f(x, z, t, n):
    return 0

f = FUNTYPE(f)

mylib.test(f)
</code>
The error I get is:
<code>Traceback (most recent call last):
  File "test.py", line 18, in &lt;module&gt;
    mylib.test(f)
  File "C:\WinPython-64bit-3.5.2.3Qt5\python-3.5.2.amd64\lib\ctypes\__init__.py", line 366, in __getattr__
    func = self.__getitem__(name)
  File "C:\WinPython-64bit-3.5.2.3Qt5\python-3.5.2.amd64\lib\ctypes\__init__.py", line 371, in __getitem__
    func = self._FuncPtr((name_
