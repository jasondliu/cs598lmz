import threading
# Test threading daemon
#def worker():
#    print('worker')
#    return
#
#threads = []
#for i in range(5):
#    t = threading.Thread(target=worker)
#    t.start()
#    threads.append(t)
#
#for thread in threads:
#    thread.join()

# Test threading with queue
import queue

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print('worker:', item)
        q.task_done()

q = queue.Queue()
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for i in range(100):
    q.put(i)

# block until all tasks are done
q.join()

# stop workers
for i in range(5):
    q.put(None)
for thread in threads:
    thread.join()
