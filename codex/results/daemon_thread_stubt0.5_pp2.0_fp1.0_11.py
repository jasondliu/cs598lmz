import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print("World")
    time.sleep(1)
</code>
This code prints "Hello" and "World" every second.
<code>Hello
World
Hello
World
Hello
World
...
</code>
I want to print "Hello" and "World" only once.
<code>Hello
World
</code>
How can I do that?
I am using Python 3.5.1 on Windows 10.


A:

Use a flag to stop the thread:
<code>import time
import threading

def run():
    while not done:
        print("Hello")
        time.sleep(1)

done = False
t = threading.Thread(target=run)
t.daemon = True
t.start()

while not done:
    print("World")
    time.sleep(1)

done = True
</code>
