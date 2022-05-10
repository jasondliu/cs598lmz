import threading
# Test threading daemon

def worker():
    print('worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('done')

# Test threading with queue
import queue
import threading

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)
        q.task_done()

q = queue.Queue()
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

for i in range(10):
    q.put(i)

q.join()

for i in range(5):
    q.put(None)

for thread in threads:
    thread.join()

print('done')

# Test threading.Lock
import thread
