import ctypes
ctypes.windll.shell32.IsUserAnAdmin()
#returns 0 if user is not an admin, 1 if it is, and -1 if there is an error
</code>

