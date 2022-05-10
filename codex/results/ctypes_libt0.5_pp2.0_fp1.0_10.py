import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
But none of these work. Help?


A:

<code>import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>

