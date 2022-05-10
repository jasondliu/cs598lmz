import ctypes
ctypes.windll.user32.MessageBoxW(0, "Incorrect syntax. \n\n" + str(err), "Error", 1)
