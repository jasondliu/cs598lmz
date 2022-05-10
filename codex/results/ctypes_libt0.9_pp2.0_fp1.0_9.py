import ctypes
ctypes.windll.user32.ShowCursor(1)
</code>
However, I know that if it can be manipulated with <code>windll</code> it can be reverse engineered.
Is there a way that the user can detect if the cursor has been moved? In other words, is there a way for the user to know that this code has been run?


A:

No.  If you can find a way to do it, you can make a trojan that doesn't need premission from the user.  While I can't prove it can't be done, I'm not aware of any trojans that do this.  The only time you can detect that you've been moved is when you enter a different window, in which case you know the window was moved not your cursor.

