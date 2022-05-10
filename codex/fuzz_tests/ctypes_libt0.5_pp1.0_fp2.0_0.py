import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
The above code is working only when I run the script in the python shell. If I run the script directly, the message box does not appear.

