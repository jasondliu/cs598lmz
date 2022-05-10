import sys, threading

def run():
    while True:
        print("Hello")

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print("World")
    time.sleep(1)
</code>
I want the "Hello" to be printed every second, but it doesn't work.
I tried to use <code>threading.Timer</code> but it didn't work either.
How can I do it?


A:

You can use <code>threading.Timer</code> to run a function every second.
<code>import time
import threading

def run():
    print("Hello")
    threading.Timer(1, run).start()

run()

while True:
    print("World")
    time.sleep(1)
</code>

