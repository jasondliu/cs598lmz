import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
</code>
I've also tried to use py2exe and cx_Freeze, but the issue persists.

