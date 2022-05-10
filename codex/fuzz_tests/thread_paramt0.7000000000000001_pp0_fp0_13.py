import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 以上是不确定的
ThreadPoolExecutor(max_workers=2).submit(print, 'Hello from thread 1')
ThreadPoolExecutor(max_workers=2).submit(print, 'Hello from thread 2')
# 以上是确定的，因为每个线程都有自己的线程池

from queue import Queue
from threading import Thread, Lock

# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        ...
        # Make an (data, event) pair and hand it to the consumer
        out_q.put((data, threading.Event()))

# A thread that consumes data
def consumer(in_q):
    while True:
       
