import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# import ctypes  # An included library with Python install.   
# ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)


# from ctypes import wintypes
# from ctypes import windll

# MB_OK = 0x0000
# MB_OKCANCEL = 0x0001
# MB_ABORTRETRYIGNORE = 0x0002
# MB_YESNOCANCEL = 0x0003
# MB_YESNO = 0x0004
# MB_RETRYCANCEL = 0x0005
# MB_CANCELTRYCONTINUE = 0x0006
# MB_ICONHAND = 0x0010
# MB_ICONQUESTION = 0x0020
# MB_ICONEXCLAMATION = 0x0030
# MB_ICONASTERISK = 0x0040
# MB_USERICON = 0x0080
# MB_ICONWARNING = MB_ICONEXCL
