import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()
</code>
But when I try to run this using windows task scheduler, it shows up as complete. But there is no Hello World greeting that I can see.
Desired result:
"Hello World" should appear in the command window (batch file window)


A:

When a program command is executed with no UI, the stdout stream of the process will be processed by the task scheduler (e.g. stored in a log file), but will not be shown.
So you need some extra work to see the message.
The code below also works for Python 3.x.
<code># encoding: cp1252
import sys, threading
import win32process
from ctypes import byref, create_unicode_buffer, sizeof

t = threading.Thread(target=lambda: sys.stdout.write('Hello World\n'))
t.start()
t.join()

fileHandles = win32process.STARTUPINFO()
fileHandles.dwFlags = 1
fileHandles.cb = sizeof(fileHandles)
