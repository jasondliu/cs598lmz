import ctypes
ctypes.windll.user32.MessageBoxW(None, "Message Box Title", "Message Text", 0)
</code>
Note that you can only import ctypes once. So importing the module at the top of your file is invalid.
There is also a Python module called win32api that provides a method for putting the text into the clipboard. However, it cannot be used on Windows 7 to copy text to the clipboard. It works fine on Windows XP.
I am asking how to copy text to the clipboard on Windows 7 using Python.
I am using Python 3.2 and Windows 7.


A:

The following code works on Windows 7 and Windows XP.
<code>import ctypes
ctypes.windll.user32.OpenClipboard(None)  
ctypes.windll.user32.EmptyClipboard()  
ctypes.windll.user32.SetClipboardData(1, ctypes.c_char_p("Message Text"))  
ctypes.windll.user32.CloseClipboard()
</code>

