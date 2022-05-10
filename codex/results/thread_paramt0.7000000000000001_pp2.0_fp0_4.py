import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread\n")).start()
print("main")

"""
$ python3 -q thread_main.py
thread
main
"""

# Threads share global state.
import threading, time

def countdown(n):
    global count
    while count > 0:
        count -= 1
        print("T-minus", count, "(" + threading.currentThread().getName() + ")")
        time.sleep(0.5)

count = 5
t1 = threading.Thread(target=countdown, name="thread1", args=(5,))
t2 = threading.Thread(target=countdown, name="thread2", args=(5,))
t1.start(); t2.start()
t1.join(); t2.join()
print("Done.")

"""
$ python3 -q thread_countdown.py
T-minus 4 (thread1)
T-minus 3 (thread2)
T-minus 3 (thread1)
T-minus 2 (thread2)
T-minus 2 (thread1)
T
