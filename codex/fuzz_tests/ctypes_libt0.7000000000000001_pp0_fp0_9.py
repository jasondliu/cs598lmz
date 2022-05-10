import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
works perfectly. But I need to run it without any user interaction.

