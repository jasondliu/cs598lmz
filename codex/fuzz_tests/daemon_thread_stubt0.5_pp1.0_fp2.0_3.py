import sys, threading

def run():
    while True:
        print("Hello, World!")
        time.sleep(1)

threading.Thread(target=run).start()
</code>
I have been reading about threads and I know that they are not the solution to this, but I don't know what is.


A:

You can use <code>threading.Timer</code> to run a function periodically.
<code>import time
import threading

def run():
    print("Hello, World!")

t = threading.Timer(1, run)
t.start()
</code>

