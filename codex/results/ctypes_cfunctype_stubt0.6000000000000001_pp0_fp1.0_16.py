import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun()
</code>
I get this error:
<code>Traceback (most recent call last):
  File "E:/x.py", line 7, in &lt;module&gt;
    fun()
  File "C:\Python27\lib\site-packages\ctypes\__init__.py", line 378, in __call__
    return self._function(*args)
  File "C:\Python27\lib\site-packages\ctypes\wintypes.py", line 35, in __getattr__
    func = self.__getitem__(name)
  File "C:\Python27\lib\site-packages\ctypes\wintypes.py", line 40, in __getitem__
    func = _wintypes.__getitem__(name)
KeyError: 'LONG_PTR'
</code>
While this works:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

fun()
</code>
