import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
What is the best way for the sub process to find out that the main process has exited and run the sub process code?

