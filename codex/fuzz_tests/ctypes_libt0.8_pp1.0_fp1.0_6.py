import ctypes
ctypes.windll.user32.MessageBoxW(0, "Processing Complete.\nThe program will immediately exit.", "Complete", 1)
sys.exit()
