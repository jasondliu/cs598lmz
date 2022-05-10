import sys, threading

def run():
    while True:
        print "running..."

def stop(thread):
    thread.stop()

t = threading.Thread(target=run)
t.start()

time.sleep(3)

stop(t)
</code>
I know that I can <code>sys.exit()</code> from the thread, but this is just an example, I would like to know how to stop the thread from the outside.


A:

One way would be to use a <code>threading.Event</code>:
<code>import time
import threading

def run(event):
    while not event.is_set():
        print "running..."

def stop(event):
    event.set()

event = threading.Event()
t = threading.Thread(target=run, args=(event,))
t.start()

time.sleep(3)

stop(event)
</code>

