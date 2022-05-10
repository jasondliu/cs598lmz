import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        t.join()
        sys.exit(0)
</code>
It does not matter if I press Ctrl-C once or multiple times, the program will always exit.
Is there a way to make the program wait for the thread to finish before exiting, without using <code>threading.Event</code>?
The way I know to do it is to use <code>threading.Event</code> and pass it to the thread, and then in the main thread wait for it:
<code>import time, sys, threading

def run(event):
    for i in range(10):
        print(i)
        time.sleep(1)
    event.set()

event = threading.Event()
t = threading.Thread(target=run, args=(event,))
t.start()

while True
