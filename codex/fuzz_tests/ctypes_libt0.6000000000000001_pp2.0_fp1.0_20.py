import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
This works as expected, but when I try to use a variable as the text, it doesn't work.
This works:
<code>ctypes.windll.user32.MessageBoxW(0, "Hello World", "Your title", 1)
</code>
This doesn't:
<code>text = "Hello World"
ctypes.windll.user32.MessageBoxW(0, text, "Your title", 1)
</code>


A:

<code>ctypes.windll.user32.MessageBoxW(0, text.encode('utf-8'), "Your title", 1)
</code>
You can try this way.

