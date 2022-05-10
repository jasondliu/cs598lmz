import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
This will lock the screen.
If you want to lock the screen when the pc is idle:
<code>import win32api
import win32con
import ctypes

if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
    pass
elif win32api.GetAsyncKeyState(win32con.VK_RBUTTON):
    pass
else:
    ctypes.windll.user32.LockWorkStation()
</code>

