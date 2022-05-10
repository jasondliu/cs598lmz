import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
print fun()
</code>
or
<code>from ctypes import *
@CFUNCTYPE(None)
def fun():
    return 0
print fun()
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "C:\Python27\lib\ctypes\__init__.py", line 354, in __call__
    self._flags_ &amp; FUNCFLAG_CDECL,
WindowsError: exception: access violation reading 0x00000008

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\User\Desktop\temp.py", line 10, in &lt;module&gt;
    print fun()
  File "C:\Python27\lib\ctypes\__init__.py", line 357, in __call__
    self._flags_ &amp; FUNCFLAG_PYTHONAPI,
WindowsError: exception: access violation reading 0x00000008
</code>
I'm using Python 2.7.8
