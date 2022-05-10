import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello World", "Title", 1)
</code>
which will launch modal window but what I want is a non-modal window:
<code>ctypes.windll.user32.MessageBoxW(0, "Hello World", "Title", 0)
</code>
The problem is the window doesn't show up. I've tried to use <code>time.sleep()</code> or <code>input()</code> function before <code>MessageBoxW()</code> function but still not working.
However when I use the same code in the Python console it's working:
<code>import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello World", "Title", 0)
</code>
It's working on Python 2 and 3.
Does anyone have ever faced this problem on Windows?

