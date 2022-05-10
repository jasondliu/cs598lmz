import ctypes
ctypes.windll.user32.SwitchToThisWindow(hWnd, True)
time.sleep(1)
SendKeys("{TAB}{ENTER}")
</code>
Is there some way I can rewrite this code to get it to work on a Mac?  I'm using Python 2.7 on Mac OS X 10.8.

