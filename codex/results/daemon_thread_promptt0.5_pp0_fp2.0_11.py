import threading
# Test threading daemon
import threading

def do_this():
    global x
    while True:
        lock.acquire()
        while x < 300:
            x += 1
            print(x)
        lock.release()

def do_after():
    global x
    while True:
        lock.acquire()
        while x > 0:
            x -= 1
            print(x)
        lock.release()


x = 0
lock = threading.Lock()

our_thread = threading.Thread(target=do_this, daemon=True)
our_thread2 = threading.Thread(target=do_after, daemon=True)

our_thread.start()
our_thread2.start()

our_thread.join()
our_thread2.join()
print("Done")

import threading

def do_this():
    global x
    while True:
        lock.acquire()
        while x < 300:
            x += 1
            print(x)
        lock.release()

def do_after():
    global x
    while
