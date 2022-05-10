import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import win32gui
win32gui.MessageBox(0, "Your text", "Your title", 1)
</code>
But non of these work in this case - only access denied (even when I am admin).
The reason for that is that the package executes the exe with <code>win32api.ShellExecute(0, "runas", tempFileName, vbNullString, vbNullString, win32con.SW_SHOWNORMAL)</code>
So, is there any way to make it work?


A:

Since you are using the "runas" mode, it may be that you need to use <code>win32api.ShellExecute(None, "runas", file_to_run, None, None, win32con.SW_SHOWNORMAL)</code>. Note the 'None' is used instead of 0 for the desktop argument.

