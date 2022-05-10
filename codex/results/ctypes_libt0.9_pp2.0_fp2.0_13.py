import ctypes
ctypes.windll.user32.PostMessage(self.ProtoDriverWindow.GetSafeHwnd(), WM_CLOSE, 0, 0)
</code>
Warning:
By using this code we are killing the application, so I recommend make sure you are terminating the application.

