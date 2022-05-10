import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\Users\brian.bui\Desktop\Wallpaper\wallpaper.jpg", 0)
</code>
I have tried running this script as an administrator and I have also tried disabling the lock screen, but I still get this error. 
If I run this script in my own account, it works. If I run it in another account, it works. If I run it in the administrator account, it works. I can only get this error when I run it in the Guest account.
Does anyone know how to fix this?

