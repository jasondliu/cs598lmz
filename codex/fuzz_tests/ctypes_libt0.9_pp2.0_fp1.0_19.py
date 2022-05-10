import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
and when the code is run, nothing happens, that is, there is no logout or lock. Does anyone have any ideas why this would be? I am at a loss and have tried all sorts of answers to identical questions and nothing has worked so far.
Cheers!


A:

I managed to find the solution to this so I thought, why not share it here just in case anyone has a similar issue.
I had to add an import file called "pywintypes.py" into the same file as the login.py file and then run the following code:
<code>import win32api
win32api.ExitWindowsEx(0)
</code>
This initiates the log off screen.
One more thing was needed. I wanted the log off screen to show the option of log off AND lock the computer instead of just log off. So to do this I changed the above code to:
<code>import win32api
win32api.ExitWindowsEx(1)
</code>
This provides the log off and lock option and locks the computer.

