import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
But I have no idea how to get the result from the user.
Thanks for help


A:

If you're using Python 2.x, you can use <code>ctypes.windll.user32.MessageBoxA</code> instead, which will return an integer representing the button the user clicked on.
<code>&gt;&gt;&gt; ctypes.windll.user32.MessageBoxA(0, "Click the correct button", "Click 1", 1)
1
&gt;&gt;&gt; ctypes.windll.user32.MessageBoxA(0, "Click the correct button", "Click 2", 2)
2
&gt;&gt;&gt; ctypes.windll.user32.MessageBoxA(0, "Click the correct button", "Click 3", 3)
4
</code>
The possible return values are documented here.

