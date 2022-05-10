import ctypes
ctypes.windll.user32.MessageBoxW(0, 'This is a message', 'This is a title', 1)
</code>


A:

I can't find the source for this but I remember reading somewhere that the <code>MessageBox</code> function is implemented in user32.dll.  That's why you need to call it with <code>windll</code>.

