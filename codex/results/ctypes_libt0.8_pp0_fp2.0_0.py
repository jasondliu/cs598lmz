import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello World", "Error", 1)
</code>
The above code will work if the user is logged in to the system, because of course, the command prompt can't display a GUI to the user. It's not a user-interactive process.

