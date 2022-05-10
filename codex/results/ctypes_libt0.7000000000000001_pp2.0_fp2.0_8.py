import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#the messagebox has a return value
#vbOK = 1
#vbCancel = 2
#vbAbort = 3
#vbRetry = 4
#vbIgnore = 5
#vbYes = 6
#vbNo = 7

ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
