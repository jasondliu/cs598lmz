import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
The script runs fine, but it doesn't lock the workstation.
I've tried to run the script from the command line with the same result.
I've also tried to create a shortcut with the same result.
I've tried the same script with <code>win32gui.LockWorkstation()</code> and it works fine. But I want to use <code>ctypes</code> in my script.
Any idea why it doesn't work?


A:

The LockWorkStation function is available in Windows XP and later.
You can use this function in a script only if the script is running in an enhanced security context, such as an elevated user account. If the script is running under a standard user account, the LockWorkStation function has no effect.
For more information, see Scripting in Windows.

