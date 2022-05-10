import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Threads share global state
x = 0
def increment_global():
    global x
    x += 1

def taskofthread(lock):
    for _ in range(100000):
        lock.acquire()
        increment_global()
        lock.release()

def thread_task():
    global x
    x = 0

    lock = threading.Lock()
    t1 = threading.Thread(target=taskofthread, args=(lock,))
    t2 = threading.Thread(target=taskofthread, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    thread_task()
    print("x = {1} after {0} iterations".format(i,x))

# Queues
from queue import Queue

