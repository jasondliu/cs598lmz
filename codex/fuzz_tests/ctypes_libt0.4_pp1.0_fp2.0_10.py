import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PyCalc")

# set the window size
ctypes.windll.kernel32.SetConsoleScreenBufferSize(ctypes.windll.kernel32.GetStdHandle(-11), (120, 30))

# set the font
ctypes.windll.kernel32.SetCurrentConsoleFontEx(ctypes.windll.kernel32.GetStdHandle(-11), False, ctypes.pointer(font))

# set the window size
ctypes.windll.kernel32.SetConsoleScreenBufferSize(ctypes.windll.kernel32.GetStdHandle(-11), (120, 30))

# set the window position
ctypes.windll.kernel32.SetConsoleWindowInfo(ctypes.windll.kernel32.GetStdHandle(-11), True, ctypes.byref(coord))

# set the font color
ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 0x0F)

print("""
  ____  _  _ 
