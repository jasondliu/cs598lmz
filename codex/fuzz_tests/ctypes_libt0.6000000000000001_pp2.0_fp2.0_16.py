import ctypes
ctypes.windll.user32.MessageBoxW(None, "Hello", "Title", 0)

# MessageBox function from user32.dll
user32 = ctypes.windll.user32
user32.MessageBoxW(None, "Hello", "Title", 0)
</code>

