import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

print("the first")

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

print("the second")

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

print("the third")
</code>
The problem with this code is that I want to print the first line before the first message box. I think this is because the program is running the message box code first, and then printing the print code. I have tried to do this with threads, but it has not worked.
<code>import threading
import time
import ctypes

def func():
    time.sleep(0.5)
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def func2():
    print("the first")

if __name__ == '__main__':

    t1 = threading
