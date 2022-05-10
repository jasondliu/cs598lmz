import ctypes
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
