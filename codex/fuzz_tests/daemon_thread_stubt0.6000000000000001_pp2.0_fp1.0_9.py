import sys, threading

def run():
    while True:
        print("hello")

t = threading.Thread(target=run)
t.start()

t.join()
</code>
What is the best way to kill the thread? I tried using os.kill() but it is not working.


A:

You can use a flag to communicate with the thread and make it stop:
<code>import threading
import time

def run(stop_event):
    while not stop_event.is_set():
        print("hello")
        time.sleep(0.5)

stop_event = threading.Event()
t = threading.Thread(target=run, args=(stop_event,))
t.start()

time.sleep(3)
stop_event.set()
t.join()
</code>

