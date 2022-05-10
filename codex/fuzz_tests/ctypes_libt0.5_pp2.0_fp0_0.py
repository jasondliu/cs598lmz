import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\Public\\Pictures\\Sample Pictures\\Penguins.jpg" , 0)
</code>
I also tried to add a file name to the end of the path (file.jpg), but that didn't work either.


A:

I found the answer. It seems that you need to specify the path in a certain format, which is <code>r"C:\Users\Public\Pictures\Sample Pictures\Penguins.jpg"</code>.

