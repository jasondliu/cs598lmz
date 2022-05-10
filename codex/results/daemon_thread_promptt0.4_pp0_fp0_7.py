import threading
# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Finished")

# Test threading queue

import threading
import queue

def worker(q):
    while True:
        item = q.get()
        print("Worker", item)
        q.task_done()

q = queue.Queue()

for i in range(5):
    t = threading.Thread(target=worker, args=(q,))
    t.daemon = True
    t.start()

for item in range(5):
    q.put(item)

q.join()

print("Finished")

# Test threading queue with lock

import threading
import queue
import time

def worker(q):
    while True:
        item = q.get()
        print("Worker", item)
