import ctypes
ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
</code>

...the message "Windows needs your permission to continue" is almost immediate.

