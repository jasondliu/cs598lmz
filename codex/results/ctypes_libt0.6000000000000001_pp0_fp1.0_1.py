import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# in python 3 you can use a regular string
import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# or an f-string
import ctypes
ctypes.windll.user32.MessageBoxW(0, f"Your text", f"Your title", 1)
</code>

