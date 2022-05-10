import ctypes
ctypes.windll.user32.PostMessageA(chromewin,win32con.WM_ACTIVATE,1,0)
</code>
Well, you can use win32gui, but i'm not really good using it, so i use something more 'general' like AutoHotKey, you can use something like
<code>WinActivate, Chrome
</code>
You can always ask for more if you want, but i think you could get the idea of he fisrt 2

