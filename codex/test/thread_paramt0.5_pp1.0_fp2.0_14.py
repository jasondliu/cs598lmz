import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello from thread\n")).start()

# Run a function in a thread and wait for it to finish
import threading, time

def count(n):
    while n > 0:
        n -= 1

t = threading.Thread(target=lambda: count(1000000))
t.start()
t.join()

# Run a function in a thread and wait for it to finish
import threading, time

def count(n):
    while n > 0:
        n -= 1

t = threading.Thread(target=lambda: count(1000000))
t.start()
t.join()

# Run a function in a thread and wait for it to finish
import threading, time

def count(n):
    while n > 0:
        n -= 1

t = threading.Thread(target=lambda: count(1000000))
t.start()
t.join()

# Run a function in a thread and wait for it to finish
import threading, time

