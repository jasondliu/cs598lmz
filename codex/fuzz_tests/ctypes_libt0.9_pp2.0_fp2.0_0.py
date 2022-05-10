import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(sys.argv[1])
