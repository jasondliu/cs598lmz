import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("World")
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
I would like to know if there is a way to stop the thread in the main function, and if so, how can I do it?


A:

You can use a <code>threading.Event</code> to signal the thread to stop.
<code>import time
import threading

def run(stop_event):
    while not stop_event.is_set():
        print("Hello")
        time.sleep(1)

def main():
    stop_event = threading.Event()
    thread = threading.Thread(target=run, args=(stop_event,))
    thread.start()
    try:
        while True:
            print("World")
            time.sleep(1)
    except KeyboardInterrupt:
