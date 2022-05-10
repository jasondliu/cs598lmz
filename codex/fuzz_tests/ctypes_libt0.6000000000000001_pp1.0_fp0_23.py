import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

# MessageBoxW for unicode (mixed ascii and non-ascii)
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>

