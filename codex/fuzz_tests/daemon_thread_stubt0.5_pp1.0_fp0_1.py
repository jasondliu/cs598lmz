import sys, threading

def run():
    while True:
        print('Hello, world!')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()

    while True:
        print('Goodbye, world!')
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>
I would expect this to print "Hello, world!" and "Goodbye, world!" in alternating order, but instead it prints "Hello, world!" and "Goodbye, world!" simultaneously.
How can I make it print them in alternating order?


A:

You can use <code>threading.Event</code> to communicate between threads.
<code>import threading
import time

def run(event):
    while True:
        event.wait()
        print('Hello, world!')
        time.sleep(1)
        event.clear()

def main():
    event = threading.Event()
    t = threading.Thread(target=run, args=(event,))
    t.start()


