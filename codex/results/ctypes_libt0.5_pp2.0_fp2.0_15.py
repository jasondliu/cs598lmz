import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\Users\patel\Desktop\Wallpaper\Wallpaper.jpg", 0)
</code>
This code works fine, but I want to run this code every time I start my computer. So I tried to create a task in windows task scheduler, but it doesn't work. I also tried to create a .bat file in startup folder, but it also doesn't work.
Can anyone help me how to do this?


A:

Try this:
<code>import ctypes

ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\patel\\Desktop\\Wallpaper\\Wallpaper.jpg", 0)
</code>

