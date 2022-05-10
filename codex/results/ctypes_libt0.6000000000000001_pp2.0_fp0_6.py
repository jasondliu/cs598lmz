import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>

It is a good practice to use the <code>ctypes</code> module instead of <code>win32api</code> when calling Win32 API functions.

