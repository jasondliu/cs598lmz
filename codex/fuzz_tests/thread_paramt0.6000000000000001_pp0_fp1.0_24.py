import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 2\n')).start()

# Join()
import time, threading
def counter(n):
    while n > 0:
        n -= 1
    return

# Time it
t0 = time.time()
counter(10**7)
print('Serial time:', time.time() - t0)

# Run in two threads
t0 = time.time()
t = threading.Thread(target=counter, args=(10**7//2,))
t.start()
counter(10**7//2)
t.join()
print('Parallel time:', time.time() - t0)

# Using a threading pool
import threading, queue
def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('Doing work on', item)
        q.task_done()

q = queue.Queue
