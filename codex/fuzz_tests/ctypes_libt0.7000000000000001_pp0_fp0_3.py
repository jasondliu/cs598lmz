import ctypes
ctypes.windll.user32.LockWorkStation()
</code>


A:

You can use the <code>win32gui</code> module and call <code>LockWorkStation</code> directly:
<code>import win32gui
win32gui.LockWorkStation()
</code>

