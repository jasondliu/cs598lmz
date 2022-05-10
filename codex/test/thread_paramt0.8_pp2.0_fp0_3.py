import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

def fib(n):
    return n
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib2(n):
    return n
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib2(10))

import win32console
import win32gui

win = win32console.stdout
(x, y) = win.get_origin()
(w, h) = win.get_size()
win32gui.MoveWindow(win.windowHandle, x, y, w+1, h, 1)
