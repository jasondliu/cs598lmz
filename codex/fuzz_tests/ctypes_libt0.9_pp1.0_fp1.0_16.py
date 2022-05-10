import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg", 0)
</code>
The system wallpapper image has been changed via "Settings > Personalisation". 
As you can see I am using python 3.6.


A:

You could also use <code>win32gui.SystemParametersInfo</code>.
<code>&gt;&gt;&gt; import win32api
&gt;&gt;&gt; import win32gui
&gt;&gt;&gt; import win32con
&gt;&gt;&gt; win32gui.SystemParametersInfo(
...  win32con.SPI_SETDESKWALLPAPER,
...  "path to wallpaper",
...  win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE)
</code>
W32 constants can be searched here. A list of constant and their equivalent value which you can use without <code>win32con</code> is here.

