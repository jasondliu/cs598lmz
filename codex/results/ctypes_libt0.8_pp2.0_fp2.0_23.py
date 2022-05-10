import ctypes
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "--", None, 1)
</code>
You can do the same thing calling <code>os.startfile</code> too.

