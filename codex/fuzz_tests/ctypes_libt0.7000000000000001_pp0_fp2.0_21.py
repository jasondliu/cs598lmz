import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{F11}")
</code>

