import ctypes
ctypes.windll.user32.SwitchToThisWindow(hwnd, True)

# send key
ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0) # 0x0D is 'enter'
ctypes.windll.user32.keybd_event(0x0D, 0, 0x0002, 0) # 0x0002 is 'key up'
</code>
Note:

I don't know why you want to send key to <code>cmd</code>. So I'm not sure whether this is what you want.
I think that you want to send key to <code>cmd</code> because you want to run <code>python</code> by <code>cmd</code>. So if you want to run python, how about this modification?

Modified script :
<code>import subprocess

hwnd = win32gui.FindWindow(None, "Command Prompt")
win32gui.SetForegroundWindow(hwnd)

# or
# ctypes.windll.user32.SwitchToThisWindow(hwnd, True)

# send
