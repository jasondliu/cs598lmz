import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
</code>
I would expect this to print "Hello" and "World" in an alternating fashion. However, it only prints "World".
I have tried using <code>thread.join()</code> but this does not work.
I have also tried using <code>thread.is_alive()</code> but this also does not work.
I am using Python 3.6.5 on Windows 10.
How can I get this to work?


A:

The problem is that you are printing from the main thread, and the main thread is not yielding control to the other thread.
You can fix this by using <code>time.sleep(0)</code> to yield control to the other thread.
<code>import sys, threading, time

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
   
