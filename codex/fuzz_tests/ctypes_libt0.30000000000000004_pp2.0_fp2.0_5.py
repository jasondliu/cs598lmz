import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
But I want to do this in the background, without the user having to click OK.
I know I can use <code>ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)</code> to get a message box without the OK button, but I want to do this in the background.
Is there a way to do this?


A:

You can use <code>ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)</code> to get a message box without the OK button, but I want to do this in the background.
You can use <code>ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)</code> to get a message box without the OK button, but I want to do this in the background.
You can use <code>ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)</
