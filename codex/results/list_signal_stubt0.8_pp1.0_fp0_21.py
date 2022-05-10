import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print("Tick")
    else:
        print("Done.")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

time.sleep(1)

while delays:
    time.sleep(0.5)
</code>
If you want to make this work on Windows (which doesn't have <code>itimer</code>s), you can use <code>after</code>.
<code>from Tkinter import *
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler():
    global root
    if delays:
        root.after(delays.pop() * 1000, print, "Tick")
    else:
        print("Done.")

root = Tk()
root.after(delays.pop() * 1000, handler)

root.mainloop()
</code>

