import threading
# Test threading daemon

def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Done')

# Test threading with queue

import threading
import queue

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

q = queue.Queue()
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for item in source():
    q.put(item)

q.join()       # block until all tasks are done

# Test threading with lock

import threading

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0
