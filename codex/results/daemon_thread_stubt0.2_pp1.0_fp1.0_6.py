import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
    time.sleep(1)
</code>
I would expect the output to be:
<code>World
Hello
World
Hello
World
Hello
...
</code>
But instead I get:
<code>World
World
World
World
World
...
</code>
I've tried using <code>thread.join()</code> but that just makes the program hang.
I'm using Python 3.6.3 on Windows 10.


A:

You need to flush the output:
<code>import time
import sys, threading

def run():
    while True:
        print("Hello")
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
    sys.stdout.flush()
    time.sleep(1)
