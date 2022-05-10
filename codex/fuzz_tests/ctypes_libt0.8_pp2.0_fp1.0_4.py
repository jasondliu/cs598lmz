import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello World", "In Python", 1)
</code>
I have the following code:
<code>if (message == "hello"):
    ctypes.windll.user32.MessageBoxW(0, "Hello World", "In Python", 1)
</code>
It works, but this window is only shown up one time. How to modify it to make it show up every time I type "hello"?
Thanks!


A:

It's hard to know exactly what you are doing and where the code is running, but the answer is going to be to move the call to <code>MessageBoxW()</code> outside of the conditional, like this:
<code>if message == "hello":
    # do something

ctypes.windll.user32.MessageBoxW(0, "Hello World", "In Python", 1)
</code>

