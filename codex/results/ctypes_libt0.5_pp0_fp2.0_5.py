import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Use the default Windows icon
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)

# This is the ICON_WARNING
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 48)

# This is the ICON_ERROR
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 16)
</code>

