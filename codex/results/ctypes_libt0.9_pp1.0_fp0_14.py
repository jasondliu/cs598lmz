import ctypes
ctypes.windll.user32.MessageBoxW(0, "Composite Risk Management", "Title", 1)
</code>
Unfortunately the output of <code>pyinstaller</code> is two executables which, when I try to run them, all I get is a message that <code>MSVCP100.dll</code> is missing.
I also tried to make <code>exe</code> with <code>py2exe</code> and I got the same message.
Also, I tried to do an offline installation of <code>pywin32</code> and I got the same message.
Furthermore, I tried to extract all dll files from <code>MS Visual C++ 2010 Redistributable Package (x86)</code>  and place them in my machine. But, still I got the same error.

