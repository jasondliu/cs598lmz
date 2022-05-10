import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
</code>
<code>MessageBoxA</code> is the ANSI version. If you want to use Unicode, use <code>MessageBoxW</code> instead.

