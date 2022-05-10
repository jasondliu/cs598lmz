import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('myappid')
</code>
This will allow you to have shortcut links on the taskbar and Windows 10 app menu that are separate from the Python.exe that you are running.

