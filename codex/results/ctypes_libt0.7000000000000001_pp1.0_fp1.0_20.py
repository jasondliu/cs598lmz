import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

win32gui.SetForegroundWindow(handle)

win32gui.SetWindowPos(handle,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

win32gui.SetWindowPos(handle,win32con.HWND_NOTOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

win32gui.ShowWindow(handle,win32con.SW_SHOW)


win32gui.SetForegroundWindow(handle)
</code>
But it is not working.

