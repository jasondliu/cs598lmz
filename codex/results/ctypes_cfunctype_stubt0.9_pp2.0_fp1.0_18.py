import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
res = fun()
print(res)
</code>
Here is the error message
<code>Traceback (most recent call last):
  File "C:\Users\MyUserName\Desktop\Test.py", line 1, in &lt;module&gt;
    from ctypes import *
  File "C:\Python27\lib\ctypes\__init__.py", line 7, in &lt;module&gt;
    from _ctypes import Union, Structure, Array
ImportError: DLL load failed: %1 is not a valid Win32 application.
</code>
I'm using Python 2.7 (x86)  on a Windows 7 (x64).
If relevant, the PATH value is:
<code>C:\Python27;C:\Python27\Scripts;
</code>


A:

Python is selecting the wrong library.
<code>D:\&gt;python --version
Python 2.7.11 32bit
D:\&gt;py -2.7-32 --version
Python 2.7.11 32bit
D:\&gt;py -
