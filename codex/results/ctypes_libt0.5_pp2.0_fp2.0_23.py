import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import win32api
win32api.MessageBox(0, "Your text", "Your title")

import win32gui
win32gui.MessageBox(0, "Your text", "Your title")
</code>
I am trying to use the first option, but it is not working. I am getting the error:
<code>Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Programs\Python\Python38-32\lib\ctypes\__init__.py", line 123, in WINFUNCTYPE
    return _win_functype_cache[(restype, argtypes, flags)]
KeyError: (&lt;class 'ctypes.HRESULT'&gt;, (&lt;class 'ctypes.c_int'&gt;, &lt;class 'ctypes.c_wchar_p'&gt;, &lt;class 'ctypes.c_wchar_p'&gt;, &lt;class 'ctypes
