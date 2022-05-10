import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
</code>
This will pop up a message box allowing you to write whatever you like.
Alternatively, you can use the win32com.client module.
<code>import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.Popup("Hello world")
</code>

