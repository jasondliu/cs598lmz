import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
EDIT:
The above would work in Python 3.x and would require that you have the _ctypes extension installed.

