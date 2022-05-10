import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
Or if you want to use <code>ctypes</code> to avoid the "execution of code from the Internet" warning, you can do it like this:
<code>import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>

