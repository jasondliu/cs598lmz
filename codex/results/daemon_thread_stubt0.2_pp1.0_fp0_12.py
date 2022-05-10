import sys, threading

def run():
    while True:
        print "Hello"
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print "Goodbye"
    time.sleep(1)
</code>
I would expect this to print "Hello" and "Goodbye" in an alternating fashion. However, it only prints "Goodbye".
I am running this on Windows 7.


A:

You are running into a buffering issue. 
<code>print</code> is buffered by default, so you need to flush it.
<code>import time, sys, threading

def run():
    while True:
        print "Hello"
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print "Goodbye"
    sys.stdout.flush()
    time.sleep(1)
</code>

