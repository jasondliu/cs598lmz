import sys, threading

def run():
    while True:
        try:
            print("hello world")
            time.sleep(1)
        except:
            break

threading.Thread(target=run).start()
</code>
I am using python 3.5.2.
I have tried using a daemon thread but that doesn't work either.
How can I make it so that the thread is killed when I exit out of the python shell?


A:

You can use a <code>threading.Event</code> to signal the thread to exit.
<code>import time
import threading

def run(exit_event):
    while not exit_event.is_set():
        print("hello world")
        time.sleep(1)

exit_event = threading.Event()
threading.Thread(target=run, args=(exit_event,)).start()

# wait for input
input()

# exit thread
exit_event.set()
</code>

